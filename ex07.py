#!/usr/bin/env
# -*- coding: utf-8 -*-

""" 
Learn Python the Hard Way - Exercise 7
More Printing
"""

print "Mary had a little lamb."
print "Its fleece was white as {:s}.".format('snow')
print "And everywhere that Mary went."
print "." * 10 # Can you guess what this will do?

LET_01 = "C"
LET_02 = "h"
LET_03 = "e"
LET_04 = "e"
LET_05 = "s"
LET_06 = "e"
LET_07 = "B"
LET_08 = "u"
LET_09 = "r"
LET_10 = "g"
LET_11 = "e"
LET_12 = "r"

# Watch that end=' ' argument at the end. Try removing it to see what happens.
print LET_01 + LET_02 + LET_03 + LET_04 + LET_05 + LET_06,
print LET_07 + LET_08 + LET_09 + LET_10 + LET_11 + LET_12
