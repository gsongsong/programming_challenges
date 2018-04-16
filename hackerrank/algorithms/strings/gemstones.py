#!/bin/python3

# https://www.hackerrank.com/challenges/gem-stones/problem

import sys

def gemstones(arr):
    # Complete this function
    gems = set(arr[0])
    for string in arr[1:]:
        gems &= set(string)
    return len(gems)

n = int(input().strip())
arr = []
arr_i = 0
for arr_i in range(n):
   arr_t = str(input().strip())
   arr.append(arr_t)
result = gemstones(arr)
print(result)
