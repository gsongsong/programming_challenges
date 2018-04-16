# https://www.hackerrank.com/challenges/np-array-mathematics/problem

import numpy as np

if __name__ == "__main__":
    n, m = map(int, input().strip().split())
    a = np.array([list(map(int, input().strip().split())) for i in range(n)])
    b = np.array([list(map(int, input().strip().split())) for i in range(n)])
    print(a + b)
    print(a - b)
    print(a * b)
    print(a // b)
    print(a % b)
    print(a ** b)
