#!/usr/bin/env
# -*- coding: utf-8 -*-

"""
Learn Python the Hard Way - Exercise 18
Names, Variables, Code, Functions
"""

def print_two(*args):
    """Print any two arguments."""
    arg1, arg2 = args
    print "arg1: {}, arg2 {}".format(arg1, arg2)

def print_two_again(arg1, arg2):
    """Don't need to define args like above, ya' know."""
    print "arg1: {}, arg2 {}".format(arg1, arg2)

def print_one(arg1):
    """Take one argument, print it, and Bob's your uncle."""
    print "arg1: {}".format(arg1)

def print_none():
    """This function brooks no arguments."""
    print "Nothing to see here."

print_two("Christopher", "Perry")
print_two_again("Christopher", "Perry")
print_one("Solo!")
print_none()
