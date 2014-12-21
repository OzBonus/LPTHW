#!/usr/bin/env
# -*- coding: utf-8 -*-

"""
Learn Python the Hard Way - Exercise 39
Dictionaries, Oh Lovely Dictionaries
"""

# Map US state names to their abbreviations.
STATES = {
    "Oregon":       "OR",
    "Florida":      "FL",
    "California":   "CA",
    "New York":     "NY",
    "Michigan":     "MI",
    "Ohio":         "OH",
    "Pennsylvania": "PA",
    "West Virgina": "WV",
    "Virgina":      "VA",
    "Kentucky":     "KY"
}

# Create a set of US states and some cities in them.
CITIES = {
    "CA": "San Francisco",
    "MI": "Detroit",
    "FL": "Jacksonville"
}

# Why not add some cities?
CITIES["NY"] = "New York City"
CITIES["OR"] = "Portland"
CITIES["OH"] = "Cincinnati"
CITIES["PA"] = "Pittsburgh"
CITIES["WV"] = "Charleston"
CITIES["VA"] = "Richmond"
CITIES["KY"] = "Louisville"

# Print out some cities.
print "-" * 70
print "New York has: ", CITIES["NY"]
print "Oregon has: ", CITIES["OR"]

# Print some US states.
print "-" * 70
print "Michigan's abbreviation is: ", CITIES[STATES["Michigan"]]
print "Florida's abbreviation is: ", CITIES[STATES["Florida"]]

# Print by using the STATES and then CITIES dict.
print "-" * 70
print "Michigan has: ", CITIES[STATES["Michigan"]]
print "Florida has: ", CITIES[STATES["Florida"]]

# Print every US state abbreviation.
print "-" * 70
for st, ab in STATES.items():
    print "{} is abbreviated {}.".format(st, ab)

# Print every city in every state.
print "-" * 70
for ab, ci in CITIES.items():
    print "{} has a city called {}.".format(ab, ci)

# Now do both at the same time.
print "-" * 70
for st, ab in STATES.items():
    print "{} state is abbreviated {} and has a city called {}.".format(
        st, ab, CITIES[ab])

print "-" * 70

# Safely get an abbreviation for a US state that might not be there.
STATE = STATES.get("Texas", None)

if not STATE:
    print "Sorry, no Texas."

# Get a city with a default value.
CITY = CITIES.get("TX", "Does Not Exist")
print "The city for the US state 'TX' is {}.".format(CITY)
