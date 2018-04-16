#!/bin/python3

# https://www.hackerrank.com/challenges/game-of-thrones/problem

import sys

def gameOfThrones(s):
    # Complete this function
    letters = {chr(c): 0 for c in range(ord('a'), ord('z') + 1)}
    for c in s:
        letters[c] ^= 1
    num_odds = 0
    for c in letters:
        if letters[c] % 2:
            if len(s) % 2 == 0:
                return 'NO'
            num_odds += 1
        if num_odds > 1:
            return 'NO'
    return 'YES'

s = input().strip()
result = gameOfThrones(s)
print(result)
