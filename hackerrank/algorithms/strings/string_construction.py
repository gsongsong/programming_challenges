#!/bin/python3

# https://www.hackerrank.com/challenges/string-construction/problem

import sys

def stringConstruction(s):
    # Complete this function
    cost = 0
    pool = set()
    for c in s:
        if c not in pool:
            cost += 1
            pool |= {c}
    return cost

if __name__ == "__main__":
    q = int(input().strip())
    for a0 in range(q):
        s = input().strip()
        result = stringConstruction(s)
        print(result)
