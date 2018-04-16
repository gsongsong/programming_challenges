#!/bin/python3

# https://www.hackerrank.com/challenges/permutation-equation/problem

import sys

def permutationEquation(p):
    # Complete this function
    return [p.index(p.index(x) + 1) + 1 for x in range(1, len(p) + 1)]

if __name__ == "__main__":
    n = int(input().strip())
    p = list(map(int, input().strip().split(' ')))
    result = permutationEquation(p)
    print ("\n".join(map(str, result)))
