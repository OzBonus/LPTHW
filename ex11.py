#!/usr/bin/env

""" 
Learn Python the Hard Way - Exercise 11
Asking Questions
"""

print "How old are you?",
AGE = input('> ')
print "How tall are you?",
HEIGHT = input('> ')
print "How much do you weigh?",
WEIGHT = input('> ')

print "So, you're age is {}, your height is {}, and your weight is {}.".format(
    AGE, HEIGHT, WEIGHT
)

# Study drills below.
print "\nThat's interesting. I have some more questions."
print "How many dogs do you have?",
DOGS = input('> ')
print "And how many cats?",
CATS = input('> ')
print "What about fish?",
FISH = input('> ')

print "You've got {} dogs, {} cats, and {} fish, if I'm not mistaken.".format(
    DOGS, CATS, FISH
)
