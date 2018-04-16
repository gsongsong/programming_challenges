# https://www.hackerrank.com/challenges/np-shape-reshape/problem

import numpy as np

if __name__ == "__main__":
    arr = np.array(input().strip().split(), dtype=int)
    arr_new = np.reshape(arr, (3, 3))
    print(arr_new)
