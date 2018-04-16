# https://www.hackerrank.com/challenges/re-findall-re-finditer/problem

import re

if __name__ == "__main__":
    pattern = r'(?=([QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm][AEIOUaeiou][AEIOUaeiou]+[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm]))'
    prog = re.compile(pattern)
    find_res = re.findall(prog, input().strip())
    if find_res:
        for x in find_res:
            print(x[1:-1])
    else:
        print(-1)

