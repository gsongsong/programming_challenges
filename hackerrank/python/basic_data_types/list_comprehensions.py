# https://www.hackerrank.com/challenges/list-comprehensions/problem

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    print([[xi, yi, zi] for xi in range(x + 1)
                        for yi in range(y + 1)
                        for zi in range(z + 1)
                        if xi + yi + zi != n])
