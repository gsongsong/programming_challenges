#!/bin/python3

# https://www.hackerrank.com/challenges/drawing-book/problem

import sys

def solve(n, p):
    # Complete this function
    from_left = int(p / 2)
    if n % 2:
        from_right = int((n - p) / 2)
    else:
        from_right = int((n - p + 1) / 2)
    return min(from_left, from_right)

n = int(input().strip())
p = int(input().strip())
result = solve(n, p)
print(result)
