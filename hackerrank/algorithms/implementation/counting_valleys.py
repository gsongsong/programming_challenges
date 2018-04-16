#!/bin/python3

# https://www.hackerrank.com/challenges/counting-valleys/problem

import sys

def countingValleys(n, s):
    # Complete this function
    level = 0
    num_valleys = 0
    valley_started = False
    for c in s:
        if c == 'D':
            level -= 1
            if level < 0 and not valley_started:
                valley_started = True
            continue
        if c == 'U':
            level += 1
            if level == 0 and valley_started:
                valley_started = False
                num_valleys += 1
            continue
    return num_valleys

if __name__ == "__main__":
    n = int(input().strip())
    s = input().strip()
    result = countingValleys(n, s)
    print(result)
