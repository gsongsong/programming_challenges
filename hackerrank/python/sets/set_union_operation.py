# https://www.hackerrank.com/challenges/py-set-union/problem

if __name__ == "__main__":
    n1 = int(input())
    a = set(input().strip().split(' '))
    n2 = int(input())
    b = set(input().strip().split(' '))
    print(len(a | b))
