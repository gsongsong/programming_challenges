#!/bin/python3

# https://www.hackerrank.com/challenges/most-commons/problem

import sys
import collections

if __name__ == "__main__":
    s = input().strip()
    c = collections.Counter(s)
    d = dict()
    for key in c:
        val = c[key]
        if val not in d:
            d[val] = [key]
        else:
            d[val].append(key)
    l = sorted(list(d.items()), key=lambda x: x[0], reverse=True)
    num_remain = 3
    for elem in l:
        occur = elem[0]
        for letter in sorted(elem[1]):
            if not num_remain:
                exit(0)
            print(letter, occur)
            num_remain -= 1
