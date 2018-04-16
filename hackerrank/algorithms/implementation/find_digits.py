#!/bin/python3

# https://www.hackerrank.com/challenges/find-digits/problem

import sys

def findDigits(n):
    # Complete this function
    n_str = str(n)
    divisors = []
    for c in n_str:
        digit = int(c)
        if not digit:
            continue
        if digit in divisors:
            divisors.append(digit)
            continue
        if n % digit == 0:
            divisors.append(digit)
            continue
    return len(divisors)

if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        result = findDigits(n)
        print(result)
