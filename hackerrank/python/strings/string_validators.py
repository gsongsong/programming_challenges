# https://www.hackerrank.com/challenges/string-validators/problem

def has_alnum(s):
    for c in s:
        if c.isalnum():
            return True
    return False

def has_alpha(s):
    for c in s:
        if c.isalpha():
            return True
    return False

def has_digit(s):
    for c in s:
        if c.isdigit():
            return True
    return False

def has_lower(s):
    for c in s:
        if c.islower():
            return True
    return False

def has_upper(s):
    for c in s:
        if c.isupper():
            return True
    return False

if __name__ == '__main__':
    s = input()
    print(has_alnum(s))
    print(has_alpha(s))
    print(has_digit(s))
    print(has_lower(s))
    print(has_upper(s))
