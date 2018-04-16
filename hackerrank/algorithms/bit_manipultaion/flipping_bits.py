#!/bin/python3

# https://www.hackerrank.com/challenges/flipping-bits/problem

import sys

def flippingBits(N):
    # Complete this function
    flipped = 0
    for i in range(32,0,-1):
        num_shift = i - 1
        flipped |= (0 if (N >> num_shift) & 1 else 1) << num_shift
    return flipped

if __name__ == "__main__":
    T = int(input().strip())
    for a0 in range(T):
        N = int(input().strip())
        result = flippingBits(N)
        print(result)
