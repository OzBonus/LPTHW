#!/usr/bin/env

""" 
Learn Python the Hard Way - Exercise 6
Strings and Text
"""

X = "There are {:s} types of people.".format('10')
BINARY = "binary"
DO_NOT = "don't"
Y = "Those who know {:s} and those who {:s}.".format(BINARY, DO_NOT)

print X
print Y

print "I said: {:s}.".format(X)
print "I also said: '{:s}'.".format(Y)

HILARIOUS = False
JOKE_EVALUATION = "Isn't that joke so funny?! {}"

print JOKE_EVALUATION.format(HILARIOUS)

W = "This is the left side of..."
E = "a string with a right side."

print W + E
