#!/bin/python3

# https://www.hackerrank.com/challenges/beautiful-binary-string/problem

import sys

def beautifulBinaryString(b):
    # Complete this function
    num_change = 0
    i = 0
    while True:
        idx_start = max(i - 2, 0)
        idx_end = i + 1
        if idx_start >= len(b):
            break
        if b[idx_start:idx_end] == '010':
            num_change += 1
            i += 3
            continue
        i += 1
    return num_change

if __name__ == "__main__":
    n = int(input().strip())
    b = input().strip()
    result = beautifulBinaryString(b)
    print(result)
