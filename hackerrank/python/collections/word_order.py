# https://www.hackerrank.com/challenges/word-order/problem

import collections

if __name__ == "__main__":
    n = int(input())
    d = collections.OrderedDict()
    for _ in range(n):
        word = input().strip()
        if word in d:
            d[word] += 1
        else:
            d[word] = 1
    print(len(d))
    for key in d:
        print(d[key], end=' ')
