#!/usr/bin/env
# -*- coding: utf-8 -*-

"""
Learn Python the Hard Way - Exercise 31
Making Decisions
"""

print '\033[2J\033[H' # Clear the terminal window and reposition cursor.

print "You enter a dark room with doors of many colors. What shall you do?"
print "[1] Enter the pink door."
print "[2] Enter the gray door."
print "[3] Enter the fake door."
print "[4] Enter the meat door."

DOOR = raw_input('> ')

if DOOR == '1':
    print "You see a bear eating a cheesecake. What do you do?"
    print "[1] Take the cake."
    print "[2] Scream at the bear."

    BEAR = raw_input('> ')

    if BEAR == '1':
        print "The bear eats your face off. Good job!"
    elif BEAR == '2':
        print "The bear eats your legs off. Good job!"
    else:
        print "Well, doing {} is probably better. The bear runs away.".format(BEAR)

elif DOOR == '2':
    print "You stare into the endless abyss with Cthulhu's retina."
    print "[1] The sheep languished blue trains suffer."
    print "[2] Windows books dogs hands run."
    print "[3] Obey space cat disjointed languages swearing admit stranger bit dressing."

    INSANITY = raw_input('> ')

    if INSANITY == '1' or INSANITY == '2':
        print "Your body survives, occupied by a mind of jello. Good job!"
    else:
        print "The insanity rots your eyes into a pool of muck. Good job!"

elif DOOR == '3':
    print "You march into the fake door painted on the wall."
    print "You shatter your nose and bleed out. Good job!"

elif DOOR == '4':
    print "This door appears to be a living mass of some kind of flesh."
    print "[1] Try to open it anyway."
    print "[2] Take a bite."

    MEAT = raw_input('> ')

    if MEAT == '1':
        print "The door opens itself before you can put a hand on it."
        print "You briefly glimpse thousands of large, sharp teeth. Good job!"
    elif MEAT == '2':
        print "You get salmonella and die. Good job!"

else:
    print "You stumble around and fall on a knife and die. Good job!"
