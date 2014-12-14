#!/usr/bin/env
# -*- coding: utf-8 -*-

"""
Learn Python the Hard Way - Exercise 32
Loops and Lists
"""

the_count = [1, 2, 3, 4, 5]
fruits    = ['apples', 'oranges', 'pears', 'apricots']
change    = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# This first kind of for-loop goes through a list.
for n in the_count:
    print "This is count {}".format(n)

# Same as above.
for f in fruits:
    print "A fruit of type: {}".format(f)

# Check it out, we can loop through mixed lists, too.
# Fancy formatting handles it like a boss.
for i in change:
    print "I got {}.".format(i)

# We can also build lists. First, start with an empty one.
elements = []

# Then use the range function to do 0 to 5 counts.
for x in range(0, 6):
    print "Adding {} to the list.".format(x)
    # Append is a function that lists understand.
    elements.append(x)

# Now we can print them out, too.
for e in elements:
    print "Element was: {}".format(e)
