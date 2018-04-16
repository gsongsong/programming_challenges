#!/bin/python3

# https://www.hackerrank.com/challenges/pangrams/problem

import sys

letters = [chr(x) for x in range(ord('a'), ord('z') + 1)]

def is_pangram(s):
    # Complete this function
    for c in s:
        c_lower = c.lower()
        if c_lower in letters:
            letters.remove(c_lower)
        if not letters:
            return 'pangram'
    return 'not pangram'

if __name__ == "__main__":
    string = input().strip()
    result = is_pangram(string)
    print(result)
