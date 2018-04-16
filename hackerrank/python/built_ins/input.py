#!/bin/python2

# https://www.hackerrank.com/challenges/input/problem

if __name__ == "__main__":
    x, k = map(int, raw_input().strip().split(' '))
    if input() == k:
        print(True)
    else:
        print(False)
