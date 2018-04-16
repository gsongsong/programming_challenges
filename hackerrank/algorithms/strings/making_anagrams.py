#!/bin/python3

# https://www.hackerrank.com/challenges/making-anagrams/problem

import sys

def makingAnagrams(s1, s2):
    # Complete this function
    letters = {chr(c): 0 for c in range(ord('a'), ord('z') + 1)}
    for c in s1:
        letters[c] += 1
    for c in s2:
        letters[c] -= 1
    return sum([abs(letters[c]) for c in letters])

s1 = input().strip()
s2 = input().strip()
result = makingAnagrams(s1, s2)
print(result)
