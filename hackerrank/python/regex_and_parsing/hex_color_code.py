# https://www.hackerrank.com/challenges/hex-color-code/problem

import re

if __name__ == '__main__':
    pattern = r'.+?(#([0-9a-fA-F]{3}){1,2})'
    prog = re.compile(pattern)

    n = int(input())
    for _ in range(n):
        line = input().strip()
        result = prog.findall(line)
        if not result:
            continue
        for elem in result:
            print(elem[0])
