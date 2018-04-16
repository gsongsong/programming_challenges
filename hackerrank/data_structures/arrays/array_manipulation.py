# https://www.hackerrank.com/challenges/crush/problem

#!/bin/python3

import os
import sys

#
# Complete the arrayManipulation function below.
#
def arrayManipulation(l, query):
    #
    # Write your code here.
    #
    l[query[0] - 1] += query[2]
    if query[1] < len(l):
        l[query[1]] -= query[2]

if __name__ == '__main__':
    n, m = map(int, input().split())
    l, num_max, s = [0] * n, 0, 0
    for _ in range(m):
        arrayManipulation(l, list(map(int, input().rstrip().split())))
    for item in l:
        s += item
        if s > num_max:
            num_max = s
    print(num_max)
