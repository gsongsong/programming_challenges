#!/bin/python3

# https://www.hackerrank.com/challenges/quicksort1/problem

import sys

def quickSort(arr):
    # Complete this function
    p = arr[0]
    left = []
    right = []
    for elem in arr[1:]:
        if elem < p:
            left.append(elem)
        else:
            right.append(elem)
    return left + [p] + right


if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    result = quickSort(arr)
    print (" ".join(map(str, result)))
