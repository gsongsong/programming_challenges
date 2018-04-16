#!/bin/python3

# https://www.hackerrank.com/challenges/missing-numbers/problem

import sys

def missingNumbers(arr, brr):
    # Complete this function
    for a in arr:
        brr.remove(a)
    return sorted(list(set(brr)))

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    m = int(input().strip())
    brr = list(map(int, input().strip().split(' ')))
    result = missingNumbers(arr, brr)
    print (" ".join(map(str, result)))
