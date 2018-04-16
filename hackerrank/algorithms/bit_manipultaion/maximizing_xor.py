#!/bin/python3

# https://www.hackerrank.com/challenges/maximizing-xor/problem

import sys
import math

def bitsize(b):
    return math.floor(math.log2(b))

def maximizingXor(l, r):
    # Complete this function
    lsize, rsize = bitsize(l), bitsize(r)
    exp_common = max(lsize, rsize) + 1
    exp_curr = exp_common - 1
    while True:
        if l & (2 ** exp_curr) == r & (2 ** exp_curr):
            exp_common = exp_curr
            exp_curr -= 1
        else:
            break
    return 2 ** exp_common - 1

if __name__ == "__main__":
    l = int(input().strip())
    r = int(input().strip())
    result = maximizingXor(l, r)
    print(result)
