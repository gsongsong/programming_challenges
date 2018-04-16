# https://www.hackerrank.com/challenges/py-set-add/problem

if __name__ == "__main__":
    N = int(input())
    s = set()
    for _ in range(N):
        s.add(input().strip())
    print(len(s))
