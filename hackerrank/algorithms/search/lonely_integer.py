#!/bin/python3

# https://www.hackerrank.com/challenges/lonely-integer/problem

import sys

def lonelyinteger(a):
    # Complete this function
    d = {}
    for elem in a:
        if elem in d:
            del d[elem]
        else:
            d[elem] = 1
    return d.popitem()[0]

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
result = lonelyinteger(a)
print(result)
