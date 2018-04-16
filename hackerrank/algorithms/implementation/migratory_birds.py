#!/bin/python3

# https://www.hackerrank.com/challenges/migratory-birds/problem

import sys

def migratoryBirds(n, ar):
    # Complete this function
    birds = {key: 0 for key in range(1, 5 + 1)}
    key_max_birds = 0
    num_max_birds = 0
    for bird in ar:
        birds[bird] += 1
        if birds[bird] > num_max_birds:
            num_max_birds = birds[bird]
            key_max_birds = bird
            continue
        if birds[bird] == num_max_birds and bird < key_max_birds:
            key_max_birds = bird
    return key_max_birds

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = migratoryBirds(n, ar)
print(result)
