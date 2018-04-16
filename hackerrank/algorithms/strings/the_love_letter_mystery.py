#!/bin/python3

# https://www.hackerrank.com/challenges/the-love-letter-mystery/problem

import sys
import math

def theLoveLetterMystery(s):
    # Complete this function
    num_op = 0
    max_left = math.floor(len(s) / 2)
    for i in range(max_left):
        num_op += abs(ord(s[-1-i]) - ord(s[i]))
    return num_op

q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    result = theLoveLetterMystery(s)
    print(result)
