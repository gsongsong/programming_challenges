#!/bin/python3

# https://www.hackerrank.com/challenges/repeated-string/problem

import sys

def repeatedString(s, n):
    # Complete this function
    n_word = int(n / len(s))
    n_letters = n % len(s)

    a_in_word = 0
    a_in_letter = 0
    for i in range(len(s)):
        if s[i] == 'a':
            a_in_word += 1
            if i < n_letters:
                a_in_letter += 1
    return a_in_word * n_word + a_in_letter

if __name__ == "__main__":
    s = input().strip()
    n = int(input().strip())
    result = repeatedString(s, n)
    print(result)
