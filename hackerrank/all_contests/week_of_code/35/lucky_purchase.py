#!/bin/python3

# https://www.hackerrank.com/contests/w35/challenges/lucky-purchase

import sys

if __name__ == "__main__":
    n = int(input().strip())
    book = -1
    price_min = -1
    for a0 in range(n):
        name, value = input().strip().split(' ')
        name, value = [str(name), int(value)]
        n = {'4': 0, '7': 0}
        try:
            for c in str(value):
                if c != '4' and c != '7':
                    raise Exception
                n[c] += 1
        except Exception:
            continue
        if n['4'] != n['7'] or n['4'] == 0 or n['7'] == 0:
            continue
        if price_min == -1 or value < price_min:
            book = name
            price_min = value
    print(book)
