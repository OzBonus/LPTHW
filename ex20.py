#!/usr/bin/env
# -*- coding: utf-8 -*-

"""
Learn Python the Hard Way - Exercise 20
Functions and Files
"""

from sys import argv

SCRIPT, INPUT_FILE = argv

def print_all(f):
    print f.read()

def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    print line_count, f.readline()

CURRENT_FILE = open(INPUT_FILE)

print "First let's print the whole file.\n"
print_all(CURRENT_FILE)

print "Now let's rewind. It's kind of like a tape."
rewind(CURRENT_FILE)

print "Let's print three lines:"
CURRENT_LINE = 1
print_a_line(CURRENT_LINE, CURRENT_FILE)

CURRENT_LINE += 1
print_a_line(CURRENT_LINE, CURRENT_FILE)

CURRENT_LINE += 1
print_a_line(CURRENT_LINE, CURRENT_FILE)
