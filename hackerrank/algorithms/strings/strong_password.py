#!/bin/python3

# https://www.hackerrank.com/challenges/strong-password/problem

import sys

special_chars = '"!@#$%^&*()-+'

def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    n_for_len = max(6 - len(password), 0)
    n_for_digit = 1
    n_for_lower = 1
    n_for_upper = 1
    n_for_special = 1
    for c in password:
        if not n_for_digit and not n_for_lower and \
           not n_for_upper and not n_for_special:
            break
        if n_for_digit and c.isdigit():
            n_for_digit = 0
        if n_for_lower and c.islower():
            n_for_lower = 0
        if n_for_upper and c.isupper():
            n_for_upper = 0
        if n_for_special and c in special_chars:
            n_for_special = 0
    return max(n_for_len, n_for_digit + n_for_lower + n_for_upper + n_for_special)

if __name__ == "__main__":
    n = int(input().strip())
    password = input().strip()
    answer = minimumNumber(n, password)
    print(answer)
