#!/bin/python3

# https://www.hackerrank.com/challenges/caesar-cipher-1/problem

import sys

def ord_wrap(ord_new, ord_start, ord_end):
    ord_diff = ((ord_new - ord_end - 1) % 26)
    return ord_start + ord_diff

def caesarCipher(s, k):
    # Complete this function
    cipher = ''
    for c in s:
        if not c.isalpha():
            cipher += c
            continue
        ord_new = ord(c) + k
        if c.islower() and ord_new > ord('z'):
            ord_new = ord_wrap(ord_new, ord('a'), ord('z'))
        if c.isupper() and ord_new > ord('Z'):
            ord_new = ord_wrap(ord_new, ord('A'), ord('Z'))
        cipher += chr(ord_new)
    return cipher

if __name__ == "__main__":
    n = int(input().strip())
    s = input().strip()
    k = int(input().strip())
    result = caesarCipher(s, k)
    print(result)
