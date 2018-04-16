# https://www.hackerrank.com/challenges/validating-the-phone-number/problem

import re

if __name__ == "__main__":
    pattern = '^[789]\d{9}$'
    prog = re.compile(pattern)
    for _ in range(int(input())):
        print('YES' if prog.match(input().strip()) else 'NO')
