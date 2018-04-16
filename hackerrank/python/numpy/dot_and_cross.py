# https://www.hackerrank.com/challenges/np-dot-and-cross/problem

import numpy as np

if __name__ == "__main__":
    n = int(input())
    a = np.array([input().strip().split() for i in range(n)], dtype=int)
    b = np.array([input().strip().split() for i in range(n)], dtype=int)
    print(np.dot(a, b))
