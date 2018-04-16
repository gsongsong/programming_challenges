# https://www.hackerrank.com/challenges/np-transpose-and-flatten/problem

import numpy as np

if __name__ == "__main__":
    n, m = map(int, input().strip().split())
    arr = []
    for i in range(n):
        arr.append(list(map(int, input().strip().split())))
    mat = np.array(arr)
    print(np.transpose(mat))
    print(mat.flatten())
