# https://www.hackerrank.com/challenges/np-polynomials/problem

import numpy as np

if __name__ == "__main__":
    print(np.polyval(list(map(float, input().strip().split())), float(input())))
