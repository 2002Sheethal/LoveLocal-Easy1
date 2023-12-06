# -*- coding: utf-8 -*-
"""
Given a string s consisting of words and spaces, return the length of the last word in the string.
"""

def last_word_len(s):
    words = s.split()
    if not words:
        return 0
    return len(words[-1])


s = input("Enter the string")
result = last_word_len(s)
print(result)
