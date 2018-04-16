#!/bin/python3

# https://www.hackerrank.com/challenges/icecream-parlor/problem

import sys

def icecreamParlor(m, arr):
    # Complete this function
    for idx1 in range(len(arr)):
        first = arr[idx1]
        second = m - first
        offset = idx1 + 1
        try:
            idx2 = arr[offset:].index(second)
        except ValueError:
            continue
        return [idx1+1, offset+idx2+1]

if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        m = int(input().strip())
        n = int(input().strip())
        arr = list(map(int, input().strip().split(' ')))
        result = icecreamParlor(m, arr)
        print (" ".join(map(str, result)))
