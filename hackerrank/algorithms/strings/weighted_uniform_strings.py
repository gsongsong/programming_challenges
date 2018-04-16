#!/bin/python3

# https://www.hackerrank.com/challenges/weighted-uniform-string/problem

import sys

def weight(c):
    return ord(c) - ord('a') + 1

def update_weight_count(d, w, run):
    if w not in d:
        d[w] = run
    else:
        d[w] = max(d[w], run)

def build_weight_count(s):
    d = dict()
    w_curr = weight(s[0])
    run_curr  = 1
    d[w_curr] = 1
    for c in s[1:]:
        w = weight(c)
        if w == w_curr:
            run_curr += 1
            continue
        update_weight_count(d, w_curr, run_curr)
        w_curr = w
        run_curr = 1
    update_weight_count(d, w_curr, run_curr)
    return d

def exist_uniform_substr(weight, weight_count):
    for key in weight_count:
        if weight % key:
            continue
        if int(weight / key) <= weight_count[key]:
            return True
    return False

s = input().strip()
weight_count = build_weight_count(s)
n = int(input().strip())
for a0 in range(n):
    x = int(input().strip())
    # your code goes here
    print('Yes' if exist_uniform_substr(x, weight_count) else 'No')
