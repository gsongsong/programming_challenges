#!/bin/python3

# https://www.hackerrank.com/challenges/strange-advertising/problem

import sys

def viralAdvertising(n):
    # Complete this function
    n_curr = 1
    like_curr = 2
    likes = 2
    while n_curr < n:
        like_curr = int(like_curr * 3 / 2)
        likes += like_curr
        n_curr += 1
    return likes

if __name__ == "__main__":
    n = int(input().strip())
    result = viralAdvertising(n)
    print(result)
