#!/bin/python3

# https://www.hackerrank.com/challenges/anagram/problem

import sys
import math

def anagram(s):
    # Complete this function
    if len(s) % 2:
        return -1
    middle = math.floor(len(s) / 2)
    s1 = s[:middle]
    s2 = s[middle:]
    letters = dict()
    for i, j in zip(s1, s2):
        if i in letters:
            letters[i] += 1
        else:
            letters[i] = 1
        if j in letters:
            letters[j] -= 1
        else:
            letters[j] = -1
    return math.floor(sum([abs(letters[i]) for i in letters]) / 2)

q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    result = anagram(s)
    print(result)
