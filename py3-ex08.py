#!/usr/bin/env

""" 
Learn Python the Hard Way - Exercise 8
Printing, Printing
Python 3 Version
"""

FORMATTER = "{} {} {} {}"

print(FORMATTER.format(1, 2, 3, 4))
print(FORMATTER.format('one', 'two', 'three', 'four'))
print(FORMATTER.format(True, False, True, False))
print(FORMATTER.format(FORMATTER, FORMATTER, FORMATTER, FORMATTER))
print(FORMATTER.format(
    "I had this thing.",
    "Thay you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
    )
)
