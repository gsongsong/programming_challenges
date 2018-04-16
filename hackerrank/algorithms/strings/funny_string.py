#!/bin/python3

# https://www.hackerrank.com/challenges/funny-string/problem

import sys

def funnyString(s):
    # Complete this function
    for i in range(1, len(s)):
        if abs(ord(s[i]) - ord(s[i-1])) != abs(ord(s[-i-1]) - ord(s[-i])):
            return 'Not Funny'
    return 'Funny'

q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    result = funnyString(s)
    print(result)
