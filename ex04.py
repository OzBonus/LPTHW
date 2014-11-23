#!/usr/bin/env

""" 
Learn Python the Hard Way - Exercise 4
Variables and Names
"""

CARS = 100
SPACE_IN_A_CAR = 4.0
DRIVERS = 30
PASSENGERS = 90
CARS_NOT_DRIVEN = CARS - DRIVERS
CARS_DRIVEN = DRIVERS
CARPOOL_CAPACITY = CARS_DRIVEN * SPACE_IN_A_CAR
AVERAGE_PASSENGERS_PER_CAR = PASSENGERS / CARS_DRIVEN

print "There are", CARS, "cars available."
print "There are only", DRIVERS, "drivers available."
print "There will be", CARS_NOT_DRIVEN, "empty cars today."
print "We can transport", CARPOOL_CAPACITY, "people today."
print "We have", PASSENGERS, "to carpool today."
print "We need to put about", AVERAGE_PASSENGERS_PER_CAR, "in each car."
