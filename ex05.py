#!/usr/bin/env
# -*- coding: utf-8 -*-

""" 
Learn Python the Hard Way - Exercise 5
More Variables and Printing
"""

PERSON = 'Christopher J. Perry'
AGE = 32 # Never too old.
HEIGHT = 71 # inches
WEIGHT = 180 # pounds
EYES = 'Blue'
TEETH = 'White'
HAIR = 'Brown'

print "Let's talk about {:s}.".format(PERSON)
print "He's {:.0f} centimeters tall.".format(HEIGHT * 2.54)
print "He's {:.0f} kilograms heavy.".format(WEIGHT * 0.453592)
print "Actually that's not too heavy."
print "He's got {:s} eyes and {:s} hair.".format(EYES, HAIR)
print "His teeth are usually {:s} depending on the coffee.".format(TEETH)
print "If I add {:.0f}, {:.0f}, and {:.0f} I get {:.0f}.".format(
    AGE,
    HEIGHT * 2.54,
    WEIGHT * 0.453592,
    AGE + HEIGHT * 2.54 + WEIGHT * 0.453592
)
