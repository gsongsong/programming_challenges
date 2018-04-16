#!/bin/python3

# https://www.hackerrank.com/contests/w36/challenges/acid-naming

import sys

def acidNaming(acid_name):
    # Complete this function
    if acid_name.endswith('ic'):
        if acid_name.startswith('hydro'):
            return 'non-metal acid'
        else:
            return 'polyatomic acid'
    else:
        return 'not an acid'

if __name__ == "__main__":
    n = int(input().strip())
    for a0 in range(n):
        acid_name = input().strip()
        result = acidNaming(acid_name)
        print(result)
