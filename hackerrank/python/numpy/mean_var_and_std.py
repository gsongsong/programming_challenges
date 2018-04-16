# https://www.hackerrank.com/challenges/np-mean-var-and-std/problem

import numpy as np

if __name__ == "__main__":
    n, m = map(int, input().strip().split())
    mat = np.array([input().strip().split() for i in range(n)], dtype=float)
    print(np.mean(mat, axis=1))
    print(np.var(mat, axis=0))
    print(np.std(mat, axis=None))
