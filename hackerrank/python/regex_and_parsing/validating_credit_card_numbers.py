# https://www.hackerrank.com/challenges/validating-credit-card-number/problem

import re

if __name__ == '__main__':
    pattern = r'^[456][0-9]{3}-?[0-9]{4}-?[0-9]{4}-?[0-9]{4}$'
    prog = re.compile(pattern)
    pattern_dup = r'([0-9])-?\1-?\1-?\1'
    prog_dup = re.compile(pattern_dup)

    n = int(input())
    for _ in range(n):
        num = input().strip()
        print('Invalid' if not prog.search(num) or prog_dup.search(num) else 'Valid')
