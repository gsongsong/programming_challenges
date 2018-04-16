#!/bin/python3

# https://www.hackerrank.com/challenges/hackerrank-in-a-string/problem

import sys

def hackerrankInString(s):
    # Complete this function
    string = 'hackerrank'
    idx = 0
    for c in s:
        if c == string[idx]:
            idx += 1
        if idx == len(string):
            return 'YES'
    return 'NO'

if __name__ == "__main__":
    q = int(input().strip())
    for a0 in range(q):
        s = input().strip()
        result = hackerrankInString(s)
        print(result)
