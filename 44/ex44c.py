#!/usr/bin/env

"""
Learn Python the Hard Way - Exercise 44c
Inheritance vs. Composition
"""


class Parent(object):

    def altered(self):
        print "PARENT altered()"

class Child(Parent):

    def altered(self):
        print "CHILD, BEFORE PARENT altered()"
        super(Child, self).altered()
        print "CHILD, AFTER PARENT altered()"


DAD = Parent()
SON = Child()

DAD.altered()
SON.altered()
