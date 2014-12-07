#!/usr/bin/env
# -*- coding: utf-8 -*-

"""
Learn Python the Hard Way - Exercise 30
Else and If
"""

PEOPLE = 30 
CARS   = 40
BUSES  = 15

if CARS > PEOPLE:
    print "We should take the cars."
elif CARS < PEOPLE:
    print "We shouldn't take the cars."
else:
    print "We can't decide."

if BUSES > CARS:
    print "That's too many buses."
elif BUSES < CARS:
    print "Maybe we could still take the buses."
else:
    print "Fine! Let's just stay home!"
