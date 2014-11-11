#!/usr/bin/env

"""
Practice highlighting specific words in a text string, which ultimately
ends up being a surpise lesson in regular expressions (holy shit).
"""

import re
import colorama

colorama.init() # Enable support for ANSI escape codes on Windows.

class Passage(object):
    """Open a text file and enable highlighting of specified words."""
    
    def __init__(self, filename):
        self.filename = filename

    def raw_print(self):
        """Open a file and print its contents."""
        
        the_file = open(self.filename, 'r')   # Open the file.
        file_contents = the_file.readlines()  # Turn contents into a string.
        
        print file_contents[0]                # Print that string.
        the_file.close()

    def red_print(self):
        """Open a file, highlight a string, and print everything."""
        
        the_file = open(self.filename, 'r')
        file_contents = the_file.readlines()
        
        regex = re.compile('\\btime|too|for|who\\b', flags=re.IGNORECASE)
        
        subst = '\033[1;41m' + r'\g<0>' + '\033[0m'

        result = re.sub(regex, subst, file_contents[0])

        print result
        the_file.close()

    def highlight_story(self):
        """Print a line from a file and highlight words in a list."""
        
        the_file = open(self.filename, 'r')
        file_contents = the_file.readlines()

        # for word in highlight_terms:
        #     regex = re.compile(
        #           r'\b'      # Word boundary.
        #         + word       # Each item in the list.
        #         + r's{0,1}', # One optional 's' at the end.
        #         flags=re.IGNORECASE | re.VERBOSE)

        regex = re.compile(
              r'\b('
            + '|'.join(highlight_terms)
            + r')s?',
            flags=re.IGNORECASE | re.VERBOSE)
        subst = '\033[1;41m' + r'\g<0>' + '\033[0m'
        result = re.sub(regex, subst, file_contents[1])

        print result
        the_file.close()

    def highlight_story_looping(self):
        """Print a line from a file and highlight words in a list."""
    
        the_file = open(self.filename, 'r')
        file_contents = the_file.readlines()

        for word in highlight_terms:
            
            regex = re.compile(
                  r'\b'      # Word boundary.
                + word       # Each item in the list.
                + r's{0,1}', # One optional 's' at the end.
                flags=re.IGNORECASE | re.VERBOSE)

            subst = '\033[1;41m' + r'\g<0>' + '\033[0m'
            file_contents[1] = re.sub(regex, subst, file_contents[1])

        print file_contents[1]
        the_file.close()



highlight_terms = [
    'dog',
    'hedgehog',
    'grue'
]



INPUTTY = Passage('highlight.txt')
INPUTTY.raw_print()
INPUTTY.red_print()
INPUTTY.highlight_story()
INPUTTY.highlight_story_looping()

