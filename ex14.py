#!/usr/bin/env
# -*- coding: utf-8 -*-

"""
Learn Python the Hard Way - Exercise 14
Prompting and Passing
"""

from sys import argv

SCRIPT, USER_NAME, FAVORITE_CHEESE = argv
PROMPT = '➤ '

print "Hi {}, I'm the {} script.".format(USER_NAME, SCRIPT)
print "I'd like to ask you a few questions."
print "Do you like me, {}?".format(USER_NAME)
LIKE = raw_input(PROMPT)

print "Where do you live, {}?".format(USER_NAME)
LIVE = raw_input(PROMPT)

print "What kind of computer do you have?"
COMP = raw_input(PROMPT)

print "Right-o, so that was a big {} about liking me.".format(
    LIKE
)
print "You live in {}. I've not been there before.".format(
    LIVE
)
print "Oh, your machine is a {}. That's cool.".format(
    COMP
)
print "You like {}? I love it, too!".format(
    FAVORITE_CHEESE
)
