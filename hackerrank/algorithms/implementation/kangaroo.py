#!/bin/python3

import sys

# https://www.hackerrank.com/challenges/kangaroo/problem

def kangaroo(x1, v1, x2, v2):
    # Complete this function
    if x1 == x2:
        return 'YES'
    if v1 == v2:
        return 'NO'
    n = (x2 - x1) / (v1 - v2)
    if n < 0 or not n.is_integer():
        return 'NO'
    return 'YES'

x1, v1, x2, v2 = input().strip().split(' ')
x1, v1, x2, v2 = [int(x1), int(v1), int(x2), int(v2)]
result = kangaroo(x1, v1, x2, v2)
print(result)
