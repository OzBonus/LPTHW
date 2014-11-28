#!/usr/bin/env
# -*- coding: utf-8 -*-

"""
Learn Python the Hard Way - Exercise 16
Reading and Writing Files
"""

from sys import argv

SCRIPT, FILENAME = argv

print "The file >>{}<< will be erased.".format(FILENAME)
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
TARGET = open(FILENAME, 'w')

print "Truncating the file. Goodbye!"
TARGET.truncate()

print "Now, I'd like you to enter three lines of text."

LINE_1 = raw_input("line 1: ")
LINE_2 = raw_input("line 2: ")
LINE_3 = raw_input("line 3: ")

print "Thanks. Now to write these lines to the file."

TARGET.write(LINE_1 + '\n' + LINE_2 + '\n' + LINE_3 + '\n')

print "And finally, the file is closed."
TARGET.close()
