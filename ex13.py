#!/usr/bin/env
# -*- coding: utf-8 -*-

""" 
Learn Python the Hard Way - Exercise 13
Parameters, Unpacking, Variables
"""

from sys import argv

script, first, second, third = argv

print "The script is called:", script
print "Your first argument is:", first
print "Your second argument is:", second
print "Your third argument is:", third

# Study drills below.
print "Oh, wait a sec. Can you give me one more argument?",
ARG = raw_input('> ')
print "Thanks, buddy. Here are those arguments."
print "The script is called:", script
print "Your first argument is:", first
print "Your second argument is:", second
print "Your third argument is:", third
print "Your fourth argument is:", ARG
