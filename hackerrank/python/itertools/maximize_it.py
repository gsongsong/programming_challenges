# https://www.hackerrank.com/challenges/maximize-it/problem

import itertools

if __name__ == "__main__":
    K, M = map(int, input().strip().split(' '))
    N = []
    for _ in range(K):
        N.append(list(map(int, input().strip().split(' ')))[1:])
    sum_max = None
    for p in itertools.product(*N):
        sum_curr = sum([x ** 2 for x in p]) % M
        if not sum_max:
            sum_max = sum_curr
            continue
        if sum_curr > sum_max:
            sum_max = sum_curr
    print(sum_max)
