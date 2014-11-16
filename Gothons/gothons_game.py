"""Attack of the Grothons from Planet #25"""

# Imports.
from bs4 import BeautifulSoup
from textwrap import TextWrapper


# Classes.

class Engine(object):
    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()

        while True:
            print '-' * 70
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)


class Scene(object):

    def enter(self):
        print "Not yet configured. Subclass it and implement enter()."
        exit(1)


# The central corridor scene.
class Central(Scene):

    success = False
    
    def enter(self):
        
        if self.success == False:
            print WRAP.fill(XML.scene.central.init.string)
        
        else:
            print WRAP.fill(XML.scene.central.back.string)
        
        action = raw_input('> ')
        
        if action == 'attack':
            print WRAP.fill(XML.scene.central.die.string)
            exit(1)
        
        elif action == 'outsmart':
            print WRAP.fill(XML.scene.central.live.string)
            self.success = True
            direction = raw_input('> ')
        
            if direction == 'forward':
                return 'armory'
        
        else:
            print WRAP.fill(XML.scene.central.error.string)
            print '\n'
            return 'central'


# The armory scene.
class Armory(Scene):

    success = False

    def enter(self):
        
        if self.success == False:
            print WRAP.fill(XML.scene.armory.init.string)
        
        else:
            print WRAP.fill(XML.scene.armory.back.string)
        
        action = raw_input('> ')
        
        if action == 'sneak':
            print WRAP.fill(XML.scene.armory.die.string)
            exit(1)
        
        elif action == 'smite':
            print WRAP.fill(XML.scene.armory.live.string)
            self.success = True
            direction = raw_input('> ')
        
            if direction == 'forward':
                return 'bridge'
            
            elif direction == 'retreat':
                return 'central'
        
        else:
            print WRAP.fill(XML.scene.armory.error.string)
            print '\n'
            return 'armory'

        
class Bridge(Scene):

    success = False

    def enter(self):    
        
        if self.success == False:
            print WRAP.fill(XML.scene.bridge.init.string)
        
        else:
            print WRAP.fill(XML.scene.bridge.back.string)
        
        action = raw_input('> ')
        
        if action == 'strike':
            print WRAP.fill(XML.scene.bridge.die.string)
            exit(1)
        
        elif action == 'quaff':
            print WRAP.fill(XML.scene.bridge.live.string)
            self.success = True
            direction = raw_input('> ')

            if direction == 'forward':
                return 'pod'
        
            elif direction == 'retreat':
                return 'armory'
        
        else:
            print WRAP.fill(XML.scene.bridge.error.string)
            print '\n'
            return 'bridge'


class Pod(Scene):

    success = False
    
    def enter(self):    
        
        if self.success == False:
            print WRAP.fill(XML.scene.pod.init.string)
        
        else:
            print WRAP.fill(XML.scene.pod.back.string)
        
        action = raw_input('> ')
        
        if action == 'wet':
            print WRAP.fill(XML.scene.pod.die.string)
            exit(1)
        
        elif action == 'attack':
            print WRAP.fill(XML.scene.pod.live.string)
            self.success = True
            direction = raw_input('> ')

            if direction == 'forward':
                return 'planet'
        
            elif direction == 'retreat':
                return 'bridge'

        else:
            print WRAP.fill(XML.scene.pod.error.string)
            print '\n'
            return 'pod'


class Planet(Scene):

    def enter(self):
                
        print WRAP.fill(XML.scene.planet.init.string)
        
        action = raw_input('> ')
        
        if action == 'open':
            print WRAP.fill(XML.scene.planet.die.string)
            exit(1)
        
        elif action == 'helmet':
            print WRAP.fill(XML.scene.planet.live.string)
            exit(1)

        else:
            print WRAP.fill(XML.scene.planet.error.string)
            print '\n'
            return 'planet'


class Map(object):
    
    scenes = {
        'central': Central(),
        'armory': Armory(),
        'bridge': Bridge(),
        'pod': Pod(),
        'planet': Planet()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        return Map.scenes.get(scene_name)

    def opening_scene(self):
        return self.next_scene(self.start_scene)


# Have BeautifulSoup parse the game text file.
XML = BeautifulSoup(open('gothons_text.xml'))

# Set up text formatting.
WRAP = TextWrapper()
WRAP.initial_indent = '* '
WRAP.fix_sentence_endings = True


a_map = Map('central')
a_game = Engine(a_map)
a_game.play()

