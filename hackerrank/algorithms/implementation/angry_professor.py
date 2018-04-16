#!/bin/python3

# https://www.hackerrank.com/challenges/angry-professor/problem

import sys

def angryProfessor(k, a):
    # Complete this function
    on_time = len(a)
    for arrival in a:
        if arrival > 0:
            on_time -= 1
        if on_time < k:
            return 'YES'
    return 'NO'

if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        n, k = input().strip().split(' ')
        n, k = [int(n), int(k)]
        a = list(map(int, input().strip().split(' ')))
        result = angryProfessor(k, a)
        print(result)
