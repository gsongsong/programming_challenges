# https://www.hackerrank.com/challenges/defaultdict-tutorial/problem

import collections

if __name__ == "__main__":
    n, m = list(map(int, input().strip().split(' ')))
    d = collections.defaultdict(list)
    for i in range(1, n + 1):
        d[input().strip()].append(i)
    for i in range(m):
        l = d[input().strip()]
        if l:
            print(' '.join(map(str, l)))
        else:
            print(-1)
