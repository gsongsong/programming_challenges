#!/bin/python3

# https://www.hackerrank.com/challenges/taum-and-bday/problem

import sys

def taumBday(b, w, x, y, z):
    # Complete this function
    if x + z < y:
        return b * x + w * (x + z)
    if y + z < x:
        return b * (y + z) + w * y
    return b * x + w * y

if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        b, w = input().strip().split(' ')
        b, w = [int(b), int(w)]
        x, y, z = input().strip().split(' ')
        x, y, z = [int(x), int(y), int(z)]
        result = taumBday(b, w, x, y, z)
        print(result)
