#!/bin/python3

# https://www.hackerrank.com/challenges/the-birthday-bar/problem

import sys

def solve(n, s, d, m):
    # Complete this function
    num_cases = 0
    for i in range(len(s)):
        subseq = s[i:i+m]
        if len(subseq) != m:
            break
        if sum(subseq) == d:
            num_cases += 1
    return num_cases

n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
d, m = input().strip().split(' ')
d, m = [int(d), int(m)]
result = solve(n, s, d, m)
print(result)
