# https://www.hackerrank.com/challenges/ginorts/problem

def p(l):
    if l:
        print(l.pop(0), end='')
        p(l)

if __name__ == '__main__':
    string = input().strip()
    srt = sorted(string, key=lambda c: (not c.islower(),
                                        not c.isupper(),
                                        not c.isdigit(),
                                        c.isdigit() and not int(c) % 2,
                                        ord(c)))
    p(srt)
