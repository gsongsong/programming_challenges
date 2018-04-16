#!/bin/python3

# https://www.hackerrank.com/challenges/sherlock-and-array/problem

import sys

def solve(a):
    # Complete this function
    a.insert(0, 0)
    a.append(0)
    sum_left = a[0]
    sum_right = sum(a[2:])
    if sum_left == sum_right:
        return 'YES'
    for to_appear, to_vanish in zip(a[1:-2], a[2:-1]):
        sum_left += to_appear
        sum_right -= to_vanish
        if sum_left == sum_right:
            return 'YES'
    return 'NO'

T = int(input().strip())
for a0 in range(T):
    n = int(input().strip())
    a = list(map(int, input().strip().split(' ')))
    result = solve(a)
    print(result)
