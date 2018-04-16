# https://www.hackerrank.com/challenges/floor-ceil-and-rint/problem

import numpy as np

if __name__ == "__main__":
    arr = np.array(input().strip().split(), dtype=float)
    print(np.floor(arr))
    print(np.ceil(arr))
    print(np.rint(arr))
