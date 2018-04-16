#!/bin/python3

# https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem

import sys

def breakingRecords(score):
    # Complete this function
    maximum, break_max = score[0], 0
    minimum, break_min = score[0], 0
    for scr in score[1:]:
        if scr > maximum:
            maximum = scr
            break_max += 1
            continue
        if scr < minimum:
            minimum = scr
            break_min += 1
    return [break_max, break_min]

if __name__ == "__main__":
    n = int(input().strip())
    score = list(map(int, input().strip().split(' ')))
    result = breakingRecords(score)
    print (" ".join(map(str, result)))
