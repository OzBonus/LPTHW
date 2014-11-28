#!/usr/bin/env
# -*- coding: utf-8 -*-

"""
Learn Python the Hard Way - Exercise 17
More Files
"""

# As I did in a previous exercise, I have used the 'with' keyword to
# make dealing with files more convenient. What's cool here is that you
# can use a single 'with' statement to open multiple files, which I
# didn't know about before. Damn, that's handy.

from sys     import argv
from os.path import exists

SCRIPT, SOURCE, DESTINATION = argv

# The commented-out lines below are unnecessary fluff from the book.
# The study drill recommend taking them out.

# print "Copying from {} to {}.".format(SOURCE, DESTINATION)
# print "The input file is {} bytes long.".format(len(SOURCE))
# print "Does the output file already exists? {}".format(exists(DESTINATION))
# print "Ready! Hit RETURN to continue, CTRL-C to abort."
# raw_input()

with open(SOURCE, 'r') as ipt, open(DESTINATION, 'w') as opt:
    opt.write(ipt.read())

print "All right. Great. Wonderful. We're done here."
