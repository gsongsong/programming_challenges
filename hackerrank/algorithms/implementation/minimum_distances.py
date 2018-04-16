#!/bin/python3

# https://www.hackerrank.com/challenges/minimum-distances/problem

import sys

def minimumDistances(a):
    # Complete this function
    for d in range(1, len(a)):
        for i in range(len(a) - d):
            if abs(a[i] - a[i + d]) == 0:
                return d
    return -1

if __name__ == "__main__":
    n = int(input().strip())
    a = list(map(int, input().strip().split(' ')))
    result = minimumDistances(a)
    print(result)
