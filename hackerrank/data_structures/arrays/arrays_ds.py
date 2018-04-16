# https://www.hackerrank.com/challenges/arrays-ds/problem

#!/bin/python3

import os
import sys

#
# Complete the reverseArray function below.
#
def reverseArray(a):
    #
    # Write your code here.
    #
    return a[::-1]

if __name__ == '__main__':
    arr_count = int(input())
    arr = list(map(int, input().rstrip().split()))
    res = reverseArray(arr)
    print(' '.join(map(str, res)))
