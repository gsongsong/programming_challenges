#!/bin/python3

# https://www.hackerrank.com/challenges/the-hurdle-race/problem

import sys

def hurdleRace(k, height):
    # Complete this function
    return max(max(height) - k, 0)

if __name__ == "__main__":
    n, k = input().strip().split(' ')
    n, k = [int(n), int(k)]
    height = list(map(int, input().strip().split(' ')))
    result = hurdleRace(k, height)
    print(result)
