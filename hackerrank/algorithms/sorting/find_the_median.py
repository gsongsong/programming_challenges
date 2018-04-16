#!/bin/python3

# https://www.hackerrank.com/challenges/find-the-median/problem

import sys

def findMedian(arr):
    # Complete this function
    arr.sort()
    return arr[int(len(arr) / 2)]

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    result = findMedian(arr)
    print(result)
