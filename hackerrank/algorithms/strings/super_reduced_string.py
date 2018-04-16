#!/bin/python3

# https://www.hackerrank.com/challenges/reduced-string/problem

import sys

def reduce_helper(s):
    if not s:
        return ''

    reduced = ''
    c_curr = s[0]
    len_c = 1
    for c in s[1:]:
        if c == c_curr:
            len_c ^= 1
            continue

        reduced += c_curr * len_c
        c_curr = c
        len_c = 1
    reduced += c_curr * len_c
    return reduced

def super_reduced_string(s):
    # Complete this function
    reduced_curr = reduce_helper(s)
    while True:
        reduced_new = reduce_helper(reduced_curr)
        if reduced_curr == reduced_new:
            break
        reduced_curr = reduced_new

    return reduced_curr if reduced_curr else 'Empty String'

s = input().strip()
result = super_reduced_string(s)
print(result)
