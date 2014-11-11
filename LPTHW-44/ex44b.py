#!/usr/bin/env

""" 
Learn Python the Hard Way - Exercise 44b
Inheritance vs. Composition
"""


# Put text strings into WRAP.fill("...") if you want nice formatting.
from textwrap import TextWrapper
WRAP = TextWrapper()
WRAP.fix_sentence_endings = True


class Parent(object):

    def override(self):
        print "PARENT override()"


class Child(Parent):

    def override(self):
        print "CHILD override()"


DAD = Parent()
SON = Child()


DAD.override()
SON.override()


# The following is my own playing around.
# I'm can't be certain that the following statements are accurate.


class Socrates(object):

    def implicit(self):
        t = str(self.__class__.__name__) + " believed the greatest way to live with honor in this world is to be what we pretend to be."
        print WRAP.fill(t) + "\n"

    def override(self):
        print self.__class__.__name__, "was a classical Greek philosopher."


class Plato(Socrates):

    def override(self):
        print self.__class__.__name__, "was a Platonist."


class Aristotle(Plato):

    def override(self):
        print self.__class__.__name__, "was an Aristotleian."


class Alexander(Aristotle):

    def override(self):
        print self.__class__.__name__, "was a Macedonian King."


SOC = Socrates()
PLA = Plato()
ARI = Aristotle()
ALE = Alexander()


print '-' * 70
SOC.implicit()
SOC.override()
print '-' * 70
PLA.implicit()
PLA.override()
print '-' * 70
ARI.implicit()
ARI.override()
print '-' * 70
ALE.implicit()
ALE.override()
print '-' * 70
