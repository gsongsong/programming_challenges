# https://www.hackerrank.com/challenges/re-sub-regex-substitution/forum

import re

if __name__ == '__main__':
    pattern = r'(?<= )(&&|\|\|)(?= )'
    prog = re.compile(pattern)

    n = int(input())
    for _ in range(n):
        print(prog.sub(lambda x: 'and' if x.group() == '&&' else 'or', input()))
