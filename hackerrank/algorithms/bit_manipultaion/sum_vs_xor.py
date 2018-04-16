#!/bin/python3

# https://www.hackerrank.com/challenges/sum-vs-xor/problem

import sys

def solve(n):
    # Complete this function
    if n == 0:
        return 1
    n_bin = bin(n)[2:]
    num_zeros = 0
    for bit in n_bin:
        if bit == '0':
            num_zeros += 1
    return 2 ** num_zeros

n = int(input().strip())
result = solve(n)
print(result)
