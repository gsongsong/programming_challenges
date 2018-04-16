# https://www.hackerrank.com/challenges/np-eye-and-identity/problem

import numpy as np

if __name__ == "__main__":
    print(np.eye(*list(map(int, input().strip().split()))))
