#!/bin/python3

# https://www.hackerrank.com/challenges/countingsort2/problem

import sys

def countingSort(arr):
    # Complete this function
    counts = {}
    max_elem = 0
    for elem in arr:
        if elem in counts:
            counts[elem] += 1
        else:
            counts[elem] = 1
        if elem > max_elem:
            max_elem = elem
    ret_list = []
    for i in range(max_elem + 1):
        if i in counts:
            val = counts[i]
        else:
            val = 0
        ret_list.extend([i] * val)
    return ret_list

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    result = countingSort(arr)
    print (" ".join(map(str, result)))
