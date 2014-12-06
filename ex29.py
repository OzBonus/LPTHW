#!/usr/bin/env
# -*- coding: utf-8 -*-

"""
Learn Python the Hard Way - Exercise 29
What If
"""

PEOPLE = 20 
CATS   = 30
DOGS   = 15

if PEOPLE < CATS:
    print "Too many cats! The world is doomed!"

if PEOPLE > CATS:
    print "Not too many cats! The world is saved!"

if PEOPLE < DOGS:
    print "The world is drooled upon!"

if PEOPLE > DOGS:
    print "The world is dry!"

DOGS  += 5

if PEOPLE >= DOGS:
    print "People are greater than or equal to dogs."

if PEOPLE <= DOGS:
    print "People are less than or equal to dogs."

if PEOPLE == DOGS:
    print "People are dogs."
