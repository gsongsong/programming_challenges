# https://www.hackerrank.com/challenges/validate-list-of-email-address-with-filter/problem

import re

pattern = r'^[0-9a-zA-Z\-_]+?@[0-9a-zA-Z]+?\..{1,3}$'
prog = re.compile(pattern)

def fun(addr):
    return prog.match(addr) is not None
