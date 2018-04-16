# https://www.hackerrank.com/challenges/find-angle/problem

import cmath
import math

if __name__ == "__main__":
    ab = int(input())
    bc = int(input())
    a = complex(ab * 1j)
    c = complex(bc)
    m = (a + c) / 2
    print('{0}°'.format(math.floor(math.degrees(cmath.phase(m)) + 0.5)))
