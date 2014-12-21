#!/usr/bin/env
# -*- coding: utf-8 -*-

"""
Learn Python the Hard Way - Exercise 38
Doing Things to Lists
"""

TEN_THINGS = "Apples Oranges Crows Telephone Light Sugar"

print "\n", TEN_THINGS, "\n"
print "Hey, there aren't ten things in that list. Let's fix that.\n"

STUFF      = TEN_THINGS.split(' ')
MORE_STUFF = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(STUFF) != 10:
    next_one = MORE_STUFF.pop()
    print "Adding: ", next_one
    STUFF.append(next_one)
    print "There are {} items now.".format(len(STUFF))

print "\nThere we go: ", STUFF, "\n"

print "Let's do some things with this list of stuff.\n"

print "print stuff[1]"
print STUFF[1]

print "\nprint STUFF[-1]"
print STUFF[-1]

print "\nprint STUFF.pop()"
print STUFF.pop()

print "\nprint ' '.join(STUFF)"
print ' '.join(STUFF)

print "\nprint '#'.join(STUFF[3:5])"
print '#'.join(STUFF[3:5])

