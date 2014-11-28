#!/usr/bin/env
# -*- coding: utf-8 -*-

"""
Learn Python the Hard Way - Exercise 15
Reading Files
"""

# I did this one quite differently than what was given in the book. In
# particular, I made a point to use the 'with' keyword. The official
# docs amd other Python coders recommend doing file operations that way,
# so I figured I'd give it a shot.

from sys import argv

SCRIPT, FILE_1 = argv

with open(FILE_1, 'r') as f:
    print f.read()

print "Hey, type the filename and extension again, please"
FILE_2 = raw_input('➤ ')

with open(FILE_2, 'r') as f:
    print f.read()
