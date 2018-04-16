#!/bin/python3

# https://www.hackerrank.com/challenges/beautiful-days-at-the-movies/problem

import sys

def reversal(x):
    r = 0
    while x:
        r = r * 10 + x % 10
        x = int(x / 10)
    return r

def beautifulDays(i, j, k):
    # Complete this function
    num_days = 0
    for d in range(i, j + 1):
        if abs(d - reversal(d)) % k == 0:
            num_days += 1
    return num_days

if __name__ == "__main__":
    i, j, k = input().strip().split(' ')
    i, j, k = [int(i), int(j), int(k)]
    result = beautifulDays(i, j, k)
    print(result)
