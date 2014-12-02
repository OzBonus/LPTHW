#!/usr/bin/env
# -*- coding: utf-8 -*-

"""
Learn Python the Hard Way - Exercise 23
Read Some Code
"""

import webbrowser
import collections


URLS = collections.OrderedDict()
URLS ['Launchpad']   = 'http://www.launchpad.net'
URLS ['SourceForge'] = 'http://www.sourceforge.net'
URLS ['Freecode']    = 'http://www.freecode.com'
URLS ['Github']      = 'https://github.com/'
URLS ['RickRoll']    = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'


def menu(d):
    """Create a numbered menu from an ordered dictionary."""
    for x, y in enumerate(d):
        print "[{}] {:.<15} {}".format(x+1, y+' ', d[y])
    print

def select(d):
    """Opens a URL in an ordered list based on the number above."""
    i = int(raw_input('Enter a number: ')) - 1
    webbrowser.open_new(d.items()[i][1])
    exit(1)


print '\033[2J\033[H' # Clear the terminal window and reposition cursor.

print "This lesson doesn't have any code to type in. In place of that, the"
print "author recommends venturing out into the wilds of the Internet and"
print "looking for some Python code that is actually being used to do"
print "something useful. As an exercise for myself, I made this tiny program"
print "that allows you open in your default web browser a link that is part"
print "of the book. Just type the number next to the link.\n"
print "A few other links have been thrown in for good measure.\n"


menu(URLS)
select(URLS)
