#!/usr/bin/env
# -*- coding: utf-8 -*-

"""
Learn Python the Hard Way - Exercise 25
Even More Practice
"""

def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sort the words."""
    return sorted(words)

def print_first_word(words):
    """Pop off the first word and print it."""
    word = words.pop(0)
    print word

def print_last_word(words):
    """Pop off the last word and print it."""
    word = words.pop(-1)
    print word

def sort_sentence(sentence):
    """Accepts a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Print the initial and final words of a sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Accepts a sentence, sorts the words, print the initial and final"""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
