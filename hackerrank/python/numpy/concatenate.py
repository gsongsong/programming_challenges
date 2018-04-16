# https://www.hackerrank.com/challenges/np-concatenate/problem

import numpy as np

if __name__ == "__main__":
    n, m, p = map(int, input().strip().split())
    mat = np.array([list(map(int, input().strip().split())) for i in range(n+m)])
    print(mat)
