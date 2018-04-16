# https://www.hackerrank.com/challenges/np-sum-and-prod/problem

import numpy as np

if __name__ == "__main__":
    n, m = map(int, input().strip().split())
    mat = np.array([input().strip().split() for i in range(n)], dtype=int)
    print(np.prod(np.sum(mat, axis=0)))
