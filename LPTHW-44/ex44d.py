#!/usr/bin/env
""" 
Learn Python the Hard Way - Exercise 44d
Inheritance vs. Composition
"""


# Put text strings into WRAP.fill("...") if you want nice formatting.
from textwrap import TextWrapper
WRAP = TextWrapper()
WRAP.fix_sentence_endings = True

class Parent(object):
    """The Platonic form of this OOP lesson."""
    
    def override(self):
        print "PARENT override()"

    def implicit(self):
        print "PARENT implicit()"

    def altered(self):
        print "PARENT altered()"

class Child(Parent):
    """The trouble-making subclass."""

    def override(self):
        print "CHILD override()"
        
    def altered(self):
        print "CHILD, BEFORE PARENT altered()"
        super(Child, self).altered()
        print "CHILD, ALTERED PARENT altered()"


DAD = Parent()
SON = Child()


print '-' * 70
DAD.implicit()
SON.implicit()
print '-' * 70
DAD.override()
SON.override()
print '-' * 70
DAD.altered()
SON.altered()
print '-' * 70
