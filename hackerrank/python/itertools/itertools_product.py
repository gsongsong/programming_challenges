# https://www.hackerrank.com/challenges/itertools-product/problem

import itertools

if __name__ == "__main__":
    a = map(int, input().strip().split(' '))
    b = map(int, input().strip().split(' '))
    for t in itertools.product(a, b):
        print(t, end=' ')
