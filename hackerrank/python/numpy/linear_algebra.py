# https://www.hackerrank.com/challenges/np-linear-algebra/problem

import numpy as np

if __name__ == "__main__":
    n = int(input())
    mat = np.array([input().strip().split() for i in range(n)], dtype=float)
    print(np.linalg.det(mat))
