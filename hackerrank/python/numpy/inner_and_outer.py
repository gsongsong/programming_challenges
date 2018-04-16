# https://www.hackerrank.com/challenges/np-inner-and-outer/problem

import numpy as np

if __name__ == "__main__":
    a = np.array(input().strip().split(), dtype=int)
    b = np.array(input().strip().split(), dtype=int)
    print(np.inner(a, b))
    print(np.outer(a, b))
