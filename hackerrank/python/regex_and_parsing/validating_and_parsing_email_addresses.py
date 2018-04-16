# https://www.hackerrank.com/challenges/validating-named-email-addresses/problem

import re

if __name__ == "__main__":
    pattern = r'^[a-zA-Z][a-zA-Z0-9-_.]*@[a-zA-Z]+\.[a-zA-Z]{1,3}$'
    prog = re.compile(pattern)

    n = int(input())
    for _ in range(n):
        line = input().strip()
        idx = line.find(' ')
        name = line[:idx]
        addr = line[idx+2:-1]
        match_result = prog.match(addr)
        if match_result:
            print('{0} <{1}>'.format(name, addr))
