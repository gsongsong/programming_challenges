#!/bin/python3

# https://www.hackerrank.com/challenges/equality-in-a-array/problem

import sys

def equalizeArray(arr):
    # Complete this function
    frequency = {i: 0 for i in range(1, 101)}
    key_major = 0
    num_major = 0
    for a in arr:
        frequency[a] += 1
        if frequency[a] > num_major:
            key_major = a
            num_major = frequency[a]
    return len(arr) - num_major

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    result = equalizeArray(arr)
    print(result)
