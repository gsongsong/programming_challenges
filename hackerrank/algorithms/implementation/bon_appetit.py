#!/bin/python3

# https://www.hackerrank.com/challenges/apple-and-orange/problem

import sys

def bon_appetit(n, k, c, bill):
    # Complete this function
    bill_expected = int(sum([c[i] for i in range(len(c)) if i != k]) / 2)
    diff = bill - bill_expected
    return diff or 'Bon Appetit'

if __name__ == "__main__":
    n, k = list(map(int, input().strip().split(' ')))
    c = list(map(int, input().strip().split(' ')))
    bill = int(input().strip())
    print(bon_appetit(n, k, c, bill))
