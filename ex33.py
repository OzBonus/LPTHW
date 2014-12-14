#!/usr/bin/env
# -*- coding: utf-8 -*-

"""
Learn Python the Hard Way - Exercise 33
While-Loops
"""

# The study drills for this exercise suggested placing the while-loop in
# a function and replacing six with a variable, among other things. I
# had the intention to do just that, but also had the desire to put put
# assign a value to that variable via user input and also add some error
# checking in case there was a problem with said input. Doing this
# required such a substantial rewrite to the program that I decided to
# start it all over from scratch. Below you will see the commented-out
# code taken from this book (with minor changes) and then the code I
# created.


# COUNT   = 0
# NUMBERS = []

# while COUNT < 6:
#     print "At the top COUNT is {}".format(COUNT)
#     NUMBERS.append(i)
#     COUNT += 1
#     print "Numbers now: ", NUMBERS
#     print "At the bottom COUNT is {}".format(COUNT)

# print "The numbers: "
# for num in NUMBERS:
# print num


print '\033[2J\033[H' # Clear the terminal window and reposition cursor.


def get_input():
    """
    Get a number, check its type, and send it to the counter function.
    """
    
    try:
        print "I will populate a list with an arbitray number of integers."
        a = raw_input('> ')
        b = int(a)
    
    except Exception:
        print "There seems to be a problem with your input."
        print "-" * 70
        get_input()
    
    else:
        while_counter(b)
        for_counter(b)


def while_counter(z):
    """
    Use a while-loop to add numbers to a list from 0 up to z-1.
    """

    COUNTER = 0
    NUMBERS = []

    print '*' * 70
    print "* Initiating count using while-loop."

    while COUNTER < z:
        print "* Now adding {} to the list.".format(COUNTER)
        NUMBERS.append(COUNTER)
        print '*', NUMBERS
        COUNTER += 1

    print '*' * 70


def for_counter(y):
    """
    Use a for-loop to iterate over a list of range y to add numbers to a list.
    """

    COUNTER = 0
    NUMBERS = []

    print '#' * 70
    print "# Initiating count using for-loop."

    for x in range(y):
        print "# Now adding {} to the list.".format(COUNTER)
        NUMBERS.append(COUNTER)
        print '#', NUMBERS
        COUNTER += 1

    print '#' * 70


if __name__ == '__main__':
    get_input()