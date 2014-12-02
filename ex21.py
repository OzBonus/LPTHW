#!/usr/bin/env
# -*- coding: utf-8 -*-

"""
Learn Python the Hard Way - Exercise 22
Functions Can Return Something
"""

def add(a, b):
    print "ADDING: {} + {}".format(a, b)
    return a + b

def subtract(a, b):
    print "SUBTRACTING: {} - {}".format(a, b)
    return a - b

def multiply(a, b):
    print "MULTIPLYING: {} * {}".format(a, b)
    return a * b

def divide(a, b):
    print "DIVIDING: {} / {}".format(a, b)
    return a / b

print "Let's do some math with just functions! Damnit!"

AGE    = add(30, 5)
HEIGHT = subtract(78, 4)
WEIGHT = multiply(90, 2)
IQ     = divide(100, 2)

print "Age: {}, Height: {}, Weight: {}, IQ: {}".format(
    AGE, HEIGHT, WEIGHT, IQ
)

# A puzzle for extra credit. Just watch me type it in.
print "Here is a puzzle."

WHAT = add(AGE, subtract(HEIGHT, multiply(WEIGHT, divide(IQ, 2))))

print "That becomes:", WHAT, "Don't waste time doing it by hand."
