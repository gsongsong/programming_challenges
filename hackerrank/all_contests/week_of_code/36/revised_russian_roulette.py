#!/bin/python3

# https://www.hackerrank.com/contests/w36/challenges/revised-russian-roulette

import sys

def revisedRussianRoulette(doors):
    # Complete this function
    min_unlock = 0
    max_unlock = sum(doors)
    for i in range(len(doors)):
        if doors[i] == 1:
            min_unlock += 1
            doors[i] = 0
            if i < len(doors) - 1:
                doors[i + 1] = 0
    return min_unlock, max_unlock

if __name__ == "__main__":
    n = int(input().strip())
    doors = list(map(int, input().strip().split(' ')))
    result = revisedRussianRoulette(doors)
    print (" ".join(map(str, result)))
