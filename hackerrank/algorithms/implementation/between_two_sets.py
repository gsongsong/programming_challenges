#!/bin/python3

# https://www.hackerrank.com/challenges/between-two-sets/problem

import sys

def get_gcd(a, b):
    if a > b:
        a, b = b, a
    # a < b
    while a != 0 and b != 0:
        a, b = b % a, a
    return b

def get_lcm(a, b):
    return int(a * b / get_gcd(a, b))

def getTotalX(a, b):
    # Complete this function
    lcm = a[0]
    for elem in a[1:]:
        lcm = get_lcm(lcm, elem)
    gcd = b[0]
    for elem in b[1:]:
        gcd = get_gcd(gcd, elem)
    answers = [val for val in range(lcm, gcd + 1, lcm) if gcd % val == 0]
    return len(answers)

if __name__ == "__main__":
    n, m = input().strip().split(' ')
    n, m = [int(n), int(m)]
    a = list(map(int, input().strip().split(' ')))
    b = list(map(int, input().strip().split(' ')))
    total = getTotalX(a, b)
    print(total)
