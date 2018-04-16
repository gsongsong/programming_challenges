#!/bin/python3

# https://www.hackerrank.com/challenges/closest-numbers/problem

import sys

def closestNumbers(arr):
    # Complete this function
    arr.sort()
    pairs = [arr[0], arr[1]]
    min_diff = arr[1] - arr[0]
    for i, j in zip(arr[1:-1], arr[2:]):
        diff = j - i
        if diff == min_diff:
            pairs.append(i)
            pairs.append(j)
        elif diff < min_diff:
            pairs = [i, j]
            min_diff = diff
    return pairs

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    result = closestNumbers(arr)
    print (" ".join(map(str, result)))
