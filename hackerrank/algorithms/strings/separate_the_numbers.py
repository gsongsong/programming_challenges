#!/bin/python3

# https://www.hackerrank.com/challenges/separate-the-numbers/problem

import sys
import math

def separate_helper(s, l):
    idx = l
    num_curr = int(s[0:idx])
    while True:
        num_next = str(num_curr + 1)
        substr = s[idx:idx+len(num_next)]
        # print(num_next, substr)
        if not substr:
            return True
        if len(num_next) != len(substr):
            return False
        if num_next != substr:
            return False
        idx += len(num_next)
        num_curr += 1
    return False

def separateNumbers(s):
    # Complete this function
    for l in range(1, math.floor(len(s) / 2) + 1):
        ret = separate_helper(s, l)
        if ret:
            print('YES', s[0:l])
            return
    print('NO')

if __name__ == "__main__":
    q = int(input().strip())
    for a0 in range(q):
        s = input().strip()
        separateNumbers(s)
