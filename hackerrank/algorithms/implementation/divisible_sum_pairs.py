#!/bin/python3

# https://www.hackerrank.com/challenges/divisible-sum-pairs/problem

import sys

def divisibleSumPairs(n, k, ar):
    # Complete this function
    num_pairs = 0
    ar.sort()
    for i in range(len(ar)):
        for j in range(i+1, len(ar)):
            if (ar[i] + ar[j]) % k == 0:
                num_pairs += 1
    return num_pairs

n, k = input().strip().split(' ')
n, k = [int(n), int(k)]
ar = list(map(int, input().strip().split(' ')))
result = divisibleSumPairs(n, k, ar)
print(result)
