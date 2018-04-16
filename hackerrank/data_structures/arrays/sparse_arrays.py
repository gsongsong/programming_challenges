# https://www.hackerrank.com/challenges/sparse-arrays/problem

#!/bin/python3

import os
import sys

#
# Complete the findSuffix function below.
#
def findSuffix(collections, queryString):
    #
    # Write your code here.
    #
    num = 0
    for item in collections:
        if item == queryString:
            num += 1
    return num

if __name__ == '__main__':
    strings_count = int(input())
    strings = []
    for _ in range(strings_count):
        strings_item = input()
        strings.append(strings_item)
    q = int(input())
    for q_itr in range(q):
        queryString = input()
        res = findSuffix(strings, queryString)
        print(res)
