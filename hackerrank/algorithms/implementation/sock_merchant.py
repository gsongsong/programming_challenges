#!/bin/python3

# https://www.hackerrank.com/challenges/sock-merchant/problem

import sys

def sockMerchant(n, ar):
    # Complete this function
    socks = dict()
    num_pairs = 0
    for sock in ar:
        if sock not in socks:
            socks[sock] = 1
        else:
            socks[sock] += 1
            if socks[sock] % 2 == 0:
                num_pairs += 1
    return num_pairs

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = sockMerchant(n, ar)
print(result)
