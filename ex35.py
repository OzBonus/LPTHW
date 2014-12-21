#!/usr/bin/env
# -*- coding: utf-8 -*-

"""
Learn Python the Hard Way - Exercise 35
Branches and Functions

This is pretty similar to what's in the book, but I added another room and toyed
around for a bit with exception handling. The new death function is pretty
cool, too.
"""

from sys import exit

def start():
    """ Begin your brief, doomed adventure. """
    
    print "You are in a dark room."
    print "There are doors to the north, east, and west."
    print "[1] Go north."
    print "[2] Go east."
    print "[3] Go west."

    next = raw_input("> ")

    if next == "1":
        cthulhu_room()
    
    elif next == "2":
        broom_closet()
    
    elif next == "3":
        bear_room()

    else:
        dead("You choke on your own tongue and die.")


def cthulhu_room():
    """ What is dead can never die. """
    
    print "Here you see the great evil Cthulhu."
    print "He, it, whatever stares at you and you go insane."
    print "[1] Flee!"
    print "[2] Eat your head."

    next = raw_input("> ")

    if next == "1":
        start()
    
    elif next == "2":
        dead("Your head is high in protein.")

    else:
        cthulhu_room()


def broom_closet():
    """ A dusty old closet with a terrible secret. """

    light_on = False
    
    print "After fumbling around in the dark for a few minutes, you"
    print "realize that you have wandered into a utility closet. Being"
    print "that there's nothing much to do here, you decide that you"
    print "ought to leave, but the doorway has been lost in the darkness."
    print "[1] Look for a light switch on the wall."
    print "[2] Look for a pull-down switch hanging from the ceiling."
    print "[3] Leave the room."

    while True:

        next = raw_input("> ")

        if next == "1" and not light_on:
            dead("Scratched by a rusty nail, you get tetanus.")
        
        elif next == "1" and light_on:
            print "You already turned on the light!"
        
        elif next == "2" and not light_on:
            print "You pull a string at random and the light turns on. Lucky!"
            light_on = True

        elif next == "2" and light_on:
            dead("A second tug makes the ceiling collapse on you.")

        elif next == "3" and not light_on:
            dead("You shit your pants and die of shame.")

        elif next == "3" and light_on:
            start()

        else:
            print "You spin around for a while and feel dizzy"


def bear_room():
    """ Move a bear to proceed. """

    bear_moved = False
    
    print "A fat bear is eating honey in front of the next door."
    print "[1] Take the bear's honey."
    print "[2] Make a comment about the bear's weight."
    print "[3] Go through the door."

    while True:

        next = raw_input("> ")

        if next == "1":
            dead("The bear eats your face off.")
        
        elif next == "2" and not bear_moved:
            print "The bear moves away and sulks."
            bear_moved = True
        
        elif next == "2" and bear_moved:
            dead("The bear stops sulking and devours you.")

        elif next == "3" and not bear_moved:
            dead("You walk directly into the bear gaping jaws.")

        elif next == "3" and bear_moved:
            gold_room()

        else:
            dead("The bear slashes at you while you're dawdling.")


def gold_room():
    """ Collect a certain amount of gold and complete the game. """

    print "This room is full of gold coins. How many do you take?"

    try:
        how_much = int(raw_input("> "))
    
    except Exception:
        print "That didn't make sense. Try something else."
        gold_room()
    
    else:
        
        if how_much <= 50:
            print "Nice, you're not greedy. You win!"
            exit(0)
        else:
            dead("You die from gold poisoning.")


def dead(why):
    """ Explain cause of death (why) and exit the program. """

    print "                 ___-----------___"
    print "           __--~~                 ~~--__"
    print "       _-~~                             ~~-_"
    print "    _-~                                     ~-_"
    print "   /                                           \\"
    print "  |                                             |"
    print " |{: ^56}|".format("\033[41m"+why+"\033[0m")
    print " |                                               |"
    print "|                    \033[41mGood job!\033[0m                    |"
    print "|                                                 |"
    print "|                                                 |"
    print " |                                               |"
    print " |  |    _-------_               _-------_    |  |"
    print " |  |  /~         ~\           /~          \  |  |"
    print "  ||  |             |         |             |  ||"
    print "  || |               |       |               | ||"
    print "  || |              |         |              | ||"
    print "  |   \_           /           \           _/   |"
    print " |      ~~--_____-~    /~V~\    ~-_____--~~      |"
    print " |                    |     |                    |"
    print "|                    |       |                    |"
    print "|                    |  /^\  |                    |"
    print " |                    ~~   ~~                    |"
    print "  \_         _                       _         _/"
    print "    ~--____-~ ~\                   /~ ~-____--~"
    print "         \     /\                 /\     /"
    print "          \    | ( ,           , ) |    /"
    print "           |   | (~(__(  |  )__)~) |   |"
    print "            |   \/ (  (~~|~~)  ) \/   |"
    print "             |   |  [ [  |  ] ]  /   |"
    print "              |                     |"
    print "               \                   /"
    print "                ~-_             _-~"
    print "                   ~--___-___--~"
    exit(0)


if __name__ == '__main__':
    print "\033[2J\033[H"
    start()
