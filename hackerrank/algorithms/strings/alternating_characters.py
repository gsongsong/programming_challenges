#!/bin/python3

# https://www.hackerrank.com/challenges/alternating-characters/problem

import sys

def alternatingCharacters(s):
    # Complete this function
    num_delete = 0
    c_curr = s[0]
    for c in s[1:]:
        if c == c_curr:
            num_delete += 1
        c_curr = c
    return num_delete

q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    result = alternatingCharacters(s)
    print(result)
