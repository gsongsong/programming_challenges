# https://www.hackerrank.com/challenges/swap-case/problem

def swap_case(s):
    s_new = ''
    for c in s:
        if c.islower():
            s_new += c.upper()
        else:
            s_new += c.lower()
    return s_new
