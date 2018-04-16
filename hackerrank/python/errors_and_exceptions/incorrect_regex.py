# https://www.hackerrank.com/challenges/incorrect-regex/problem

import re

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        r = input().strip()
        try:
            re.compile(r)
            print('True')
        except:
            print('False')
