#!/bin/python3

# https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem

import sys

def jumpingOnClouds(c):
    # Complete this function
    run = 0
    jumps = 0
    for thunder in c:
        if thunder:
            jumps += int(run / 2)
            # 2-hop
            jumps += 1
            run = 0
            continue
        run += 1
    jumps += int(run / 2)
    return jumps

if __name__ == "__main__":
    n = int(input().strip())
    c = list(map(int, input().strip().split(' ')))
    result = jumpingOnClouds(c)
    print(result)
