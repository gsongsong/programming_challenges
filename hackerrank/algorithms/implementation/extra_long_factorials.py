#!/bin/python3

# https://www.hackerrank.com/challenges/extra-long-factorials/problem

import sys

def extraLongFactorials(n):
    # Complete this function
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    print(fact)

if __name__ == "__main__":
    n = int(input().strip())
    extraLongFactorials(n)
