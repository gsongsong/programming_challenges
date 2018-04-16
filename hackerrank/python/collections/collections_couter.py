# https://www.hackerrank.com/challenges/collections-counter/problem

import collections

if __name__ == "__main__":
    x = int(input())
    shoes = list(map(int, input().strip().split(' ')))
    n = int(input())
    c = collections.Counter(shoes)
    earn = 0
    for _ in range(n):
        s, p = list(map(int, input().strip().split(' ')))
        if s in c and c[s]:
            earn += p
            c[s] -= 1
    print(earn)
