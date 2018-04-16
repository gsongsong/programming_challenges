# https://www.hackerrank.com/challenges/python-time-delta/problem

import time

def strtosecond(string):
    strformattime = '%a %d %b %Y %H:%M:%S %z'
    ts = time.strptime(string, strformattime)
    off_hour = int(string[-5:-2])
    off_min = int(string[-5] + string[-2:])
    off_sec = off_hour * 3600 + off_min * 60
    return time.mktime(ts) - off_sec

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        t1 = input().strip()
        t2 = input().strip()
        print(abs(int(strtosecond(t1)) - int(strtosecond(t2))))
