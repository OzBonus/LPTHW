#!/usr/bin/env

"""
Practice printing colored text to the terminal.
"""

import random
import string
import sys
import time
import colorama

colorama.init() # Enable support for ANSI escape codes on Windows.

print '\033[2J\033[H' # Clear the terminal window and reposition cursor.
print
print '\033[30m' + 'BLACK TEXT'         + '\033[0m'
print '\033[31m' + 'RED TEXT'           + '\033[0m'
print '\033[32m' + 'GREEN TEXT'         + '\033[0m'
print '\033[33m' + 'YELLOW TEXT'        + '\033[0m'
print '\033[34m' + 'BLUE TEXT'          + '\033[0m'
print '\033[35m' + 'MAGENTA TEXT'       + '\033[0m'
print '\033[36m' + 'CYAN TEXT'          + '\033[0m'
print '\033[37m' + 'WHITE TEXT'         + '\033[0m'
print
print '\033[40m' + 'BLACK BACKGROUND'   + '\033[0m'
print '\033[41m' + 'RED BACKGROUND'     + '\033[0m'
print '\033[42m' + 'GREEN BACKGROUND'   + '\033[0m'
print '\033[43m' + 'YELLOW BACKGROUND'  + '\033[0m'
print '\033[44m' + 'BLUE BACKGROUND'    + '\033[0m'
print '\033[45m' + 'MAGENTA BACKGROUND' + '\033[0m'
print '\033[46m' + 'CYAN BACKGROUND'    + '\033[0m'
print '\033[47m' + 'WHITE BACKGROUND'   + '\033[0m'
print
print '\033[0m'  + 'ATTRIBUTES OFF'     + '\033[0m'
print '\033[1m'  + 'BOLD'               + '\033[0m'
print '\033[2m'  + 'DIM'                + '\033[0m' # No effect on Windows.
print '\033[4m'  + 'UNDERSCORE'         + '\033[0m'
print '\033[5m'  + 'BLINK'              + '\033[0m' # No effect?
print '\033[7m'  + 'INVERT COLORS'      + '\033[0m'
print '\033[8M'  + 'CONCEAL'            + '\033[0m' # No effect?

TC = [
    '\033[30m', # BLACK TEXT
    '\033[31m', # RED TEXT
    '\033[32m', # GREEN TEXT
    '\033[33m', # YELLOW TEXT
    '\033[34m', # BLUE TEXT
    '\033[35m', # MAGENTA TEXT
    '\033[36m', # CYAN TEXT
    '\033[37m', # WHITE TEXT
]

BC = [
    '\033[40m', # BLACK BACKGROUND
    '\033[41m', # RED BACKGROUND
    '\033[42m', # GREEN BACKGROUND
    '\033[43m', # YELLOW BACKGROUND
    '\033[44m', # BLUE BACKGROUND
    '\033[45m', # MAGENTA BACKGROUND
    '\033[46m', # CYAN BACKGROUND
    '\033[47m', # WHITE BACKGROUND
]

def ran_colors():
    """Print a block of random characters, colors, and backgrounds"""
    lst = []
    for _ in range(5):
        for _ in range(10):
            fore = random.choice(TC)
            back = random.choice(BC)
            char = random.choice(string.ascii_letters)
            lst.append('{}{}{}\033[m'.format(fore, back, char))
        print ''.join(lst)
        del lst[:]

def ran_line():
    """Yield a line of random characters, colors, and backgrounds"""
    while True:
        lst = []
        for _ in range(10):
            fore = random.choice(TC)
            back = random.choice(BC)
            char = random.choice(string.ascii_letters)
            lst.append('{}{}{}\033[m'.format(fore, back, char))
        yield ''.join(lst)

ran_colors()

for _ in range(50):
    sys.stdout.write(ran_line().next())
    sys.stdout.flush()
    time.sleep(0.1)
    sys.stdout.write('\b\b\b\b\b\b\b\b\b\b')
