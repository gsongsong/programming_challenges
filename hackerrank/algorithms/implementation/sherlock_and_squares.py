#!/bin/python3

# https://www.hackerrank.com/challenges/sherlock-and-squares/problem

import sys
import math

def squares(a, b):
    # Complete this function
    return len(list(range(math.ceil(math.sqrt(a)), math.floor(math.sqrt(b)) + 1)))

if __name__ == "__main__":
    q = int(input().strip())
    for a0 in range(q):
        a, b = input().strip().split(' ')
        a, b = [int(a), int(b)]
        result = squares(a, b)
        print(result)
