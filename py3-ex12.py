#!/usr/bin/env

""" 
Learn Python the Hard Way - Exercise 12
Prompting People
Python 3 Version
"""

AGE    = input("How old are you? > ")
HEIGHT = input("How tall are you? > ")
WEIGHT = input("How much do you weigh? > ")

print(
    "So, you're age is {}, your height is {}, and your weight is {}.".format(
        AGE, HEIGHT, WEIGHT
    )
)
