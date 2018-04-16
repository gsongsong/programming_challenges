#!/bin/python3

# https://www.hackerrank.com/challenges/mars-exploration/problem

import sys

def marsExploration(s):
    # Complete this function
    num_errors = 0
    for i in range(len(s)):
        if i % 3 == 0 or i % 3 == 2:
            key = 'S'
        else:
            key = 'O'
        num_errors += (s[i] != key)
    return num_errors

if __name__ == "__main__":
    s = input().strip()
    result = marsExploration(s)
    print(result)
