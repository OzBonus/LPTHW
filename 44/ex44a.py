#!/usr/bin/env

"""
Learn Python the Hard Way - Exercise 44a
Inheritance vs. Composition
"""


class Parent(object):

    def implicit(self):
        print "Parent implicit()"


class Child(Parent):
    
    pass


DAD = Parent()
SON = Child()


DAD.implicit()
SON.implicit()
