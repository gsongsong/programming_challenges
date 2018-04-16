# https://www.hackerrank.com/challenges/py-check-strict-superset/problem

if __name__ == "__main__":
    a = set(input().strip().split(' '))
    n = int(input())
    for _ in range(n):
        s = set(input().strip().split(' '))
        if len(s - a) != 0 or len(s) == len(a):
            print(False)
            exit()
    print(True)
