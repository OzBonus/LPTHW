#!/usr/bin/env
# -*- coding: utf-8 -*-

"""
Learn Python the Hard Way - Exercise 19
Functions and Variables
"""

def cheese_and_crackers(cheese_count, boxes_of_crackers):
    """Here's the function from the book."""
    print "You have {} cheeses!".format(cheese_count)
    print "You have {} boxes of crackers!".format(boxes_of_crackers)
    print "That sounds like a party!"
    print "Get a blanket. I mean that in a non-creepy way.\n"

def red_print(x, y):
    """Print a nonsense sentence and highlight some words."""
    r = "\033[32m"
    s = "\033[0m"
    print "That's a cool {}, {}.\n".format(
        r + x + s, r + y + s
    )

print "We can just define the arguments directly:"
print "cheese_and_crackers(20, 30)"
cheese_and_crackers(20, 30)

print "Or we can use variables from our script:"
print "\033[33m" + "amount_of_cheese   = 10" + "\033[0m"
print "\033[33m" + "amount_of_crackers = 10" + "\033[0m"
print "\033[33m" + "cheese_and_crackers(amount_of_cheese, amount_of_crackers)" + "\033[0m"
amount_of_cheese   = 10
amount_of_crackers = 10
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "We can do math inside, too:"
print "\033[33m" + "cheese_and_crackers(10 + 20, 5 + 6)" + "\033[0m"
cheese_and_crackers(10 + 20, 5 + 6)

print "And we can combine the two, variables and math."
print "\033[33m" + "cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)" + "\033[0m"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

print "Here's a bunch of rubbish."
print "\033[33m" + "red_print('cool', 'bro')" + "\033[0m"
red_print('story', 'bro')

print "Here's a bunch of rubbish."
print "\033[33m" + "red_print('cat ' * 3, 'bro ' * 3)" + "\033[0m"
red_print('cat ' * 3, 'bro ' * 3)
