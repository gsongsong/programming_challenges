# https://www.hackerrank.com/challenges/standardize-mobile-number-using-decorators/problem

def wrapper(f):
    def fix(num):
        return num[0:3] + ' ' + num[3:8] + ' ' + num[8:]

    def fun(l):
        # complete the function
        l_new = []
        for elem in l:
            if len(elem) == 10:
                elem = '+91' + elem
            elif len(elem) == 11:
                elem = '+91' + elem[1:]
            elif len(elem) == 12:
                elem = '+' + elem
            elif elem.startswith('+91'):
                pass
            l_new.append(fix(elem))
        return f(l_new)
    return fun
