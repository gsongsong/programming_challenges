# https://www.hackerrank.com/challenges/validating-uid/problem

import re

def validate_uid(string):
    if len(string) != 10:
        print('Invalid')
        return
    if len(set(string)) != len(string):
        print('Invalid')
        return
    pattern_upper = r'([A-Z])'
    result = re.findall(pattern_upper, string)
    if len(result) < 2:
        print('Invalid')
        return
    pattern_digit = r'([0-9])'
    result = re.findall(pattern_digit, string)
    if len(result) < 3:
        print('Invalid')
        return
    pattern_alnum = r'([0-9a-zA-Z])'
    result = re.findall(pattern_alnum, string)
    if len(result) != 10:
        print('Invalid')
        return
    print('Valid')

if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        validate_uid(input().strip())
