#!/bin/python3

# https://www.hackerrank.com/challenges/utopian-tree/problem

import sys

def utopianTree(n):
    # Complete this function
    n_curr = 0
    h = 1
    while n_curr < n:
        if n_curr % 2:
            h += 1
        else:
            h *= 2
        n_curr += 1
    return h

if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        result = utopianTree(n)
        print(result)
