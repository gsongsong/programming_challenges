# https://www.hackerrank.com/challenges/equal-stacks/problem

#!/bin/python3

import os
import sys

#
# Complete the equalStacks function below.
#
def equalStacks(s1, s2, s3):
    #
    # Write your code here.
    #
    h1, h2, h3 = sum(s1), sum(s2), sum(s3)
    while h1 != h2 or h2 != h3:
        if h1 >= h2 and h1 >= h3:
            h1 -= s1.pop(0)
        elif h2 >= h1 and h2 >= h3:
            h2 -= s2.pop(0)
        elif h3 >= h1 and h3 >= h2:
            h3 -= s3.pop(0)
    return h1

if __name__ == '__main__':
    n1, n2, n3 = map(int, input().split())
    s1 = list(map(int, input().rstrip().split()))
    s2 = list(map(int, input().rstrip().split()))
    s3 = list(map(int, input().rstrip().split()))
    print(equalStacks(s1, s2, s3))
