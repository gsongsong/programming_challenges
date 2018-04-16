#!/bin/python3

# https://www.hackerrank.com/challenges/cats-and-a-mouse/problem

import os
import sys

# Complete the catAndMouse function below.
def catAndMouse(x, y, z):
    # Write your code here.
    d1 = abs(x - z)
    d2 = abs(y - z)
    if d1 < d2:
        return 'Cat A'
    if d1 > d2:
        return 'Cat B'
    return 'Mouse C'

if __name__ == '__main__':
    q = int(input())
    for q_itr in range(q):
        xyz = input().split()
        x = int(xyz[0])
        y = int(xyz[1])
        z = int(xyz[2])
        print(catAndMouse(x, y, z))
