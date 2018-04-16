#!/bin/python3

# https://www.hackerrank.com/challenges/apple-and-orange/problem

import sys

def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Complete this function
    larry = 0
    rob = 0
    for apple in apples:
        if s <= a + apple <= t:
            larry += 1
    for orange in oranges:
        if s <= b + orange <= t:
            rob += 1
    print(larry)
    print(rob)

if __name__ == "__main__":
    s, t = input().strip().split(' ')
    s, t = [int(s), int(t)]
    a, b = input().strip().split(' ')
    a, b = [int(a), int(b)]
    m, n = input().strip().split(' ')
    m, n = [int(m), int(n)]
    apple = list(map(int, input().strip().split(' ')))
    orange = list(map(int, input().strip().split(' ')))
    countApplesAndOranges(s, t, a, b, apple, orange)
