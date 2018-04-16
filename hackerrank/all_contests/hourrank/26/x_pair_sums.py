#!/bin/python3

# https://www.hackerrank.com/contests/hourrank-26/challenges/pair-sums

import sys

def prod_nchoose2(arr):
    if len(A) == 1:
        return arr
    for i in range(len(arr)):
        for j in range(len(arr[i+1:])):
            yield arr[i] * arr[i+1:][j]

def largestValue(A):
    # Return the largest value of any of A's nonempty subarrays.
    # for prod in prod_nchoose2(A):
    #     print(prod)
    # print(sum(prod_nchoose2(A)))
    if len(A) == 1:
        return A[0]
    curr_sumprod = 0
    max_sumprod = 0
    start = 0
    end = 0
    while end < len(A):
        # print(start, end)
        subarray = A[start:end]
        sumprod = sum(prod_nchoose2(subarray))
        curr_sumprod = max(curr_sumprod, sumprod)
        max_sumprod = max(max_sumprod, curr_sumprod)
        if start == end:
            start = 0
            end += 1
            continue
        start += 1
    return max_sumprod

if __name__ == "__main__":
    n = int(input().strip())
    A = list(map(int, input().strip().split(' ')))
    result = largestValue(A)
    print(result)
