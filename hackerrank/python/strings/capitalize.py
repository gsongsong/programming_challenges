# https://www.hackerrank.com/challenges/capitalize/problem

def capitalize(string):
    l = list(string)
    c_curr = ' '
    for i in range(len(l)):
        if c_curr == ' ':
            l[i] = l[i].upper()
        c_curr = l[i]
    return ''.join(l)
