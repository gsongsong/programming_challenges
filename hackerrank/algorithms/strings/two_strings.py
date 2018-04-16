#!/bin/python3

# https://www.hackerrank.com/challenges/two-strings/problem

import sys

def twoStrings(s1, s2):
    # Complete this function
    if len(s1) < len(s2):
        src, dst = s1, s2
    else:
        src, dst = s2, s1
    for c in src:
        if c in dst:
            return 'YES'
    return 'NO'

q = int(input().strip())
for a0 in range(q):
    s1 = input().strip()
    s2 = input().strip()
    result = twoStrings(s1, s2)
    print(result)
