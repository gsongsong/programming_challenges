# https://www.hackerrank.com/challenges/2d-array/problem

#!/bin/python3

import os
import sys

#
# Complete the array2D function below.
#
def array2D(arr):
    #
    # Write your code here.
    #
    nrows, ncols = len(arr), len(arr[0])
    sum_max = -9 * 9
    for i in range(nrows - 2):
        for j in range(ncols - 2):
            sum_curr = sum(arr[i][j:j+3]) + arr[i + 1][j + 1] + sum(arr[i+2][j:j+3])
            sum_max = max(sum_max, sum_curr)
    return sum_max

if __name__ == '__main__':
    arr = []
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    result = array2D(arr)
    print(result)
