# https://www.hackerrank.com/challenges/introduction-to-regex/problem

import re

if __name__ == "__main__":
    pattern = '^[+-]?\d*\.\d+$'
    prog = re.compile(pattern)
    n = int(input())
    for _ in range(n):
        result = prog.match(input().strip())
        if result:
            print('True')
        else:
            print('False')
