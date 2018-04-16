# https://www.hackerrank.com/challenges/np-zeros-and-ones/problem

import numpy as np

if __name__ == "__main__":
    dim = tuple(map(int, input().strip().split()))
    print(np.zeros(dim, dtype=int))
    print(np.ones(dim, dtype=int))
