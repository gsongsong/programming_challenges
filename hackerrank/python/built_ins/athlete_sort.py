# https://www.hackerrank.com/challenges/python-sort-sort/problem

if __name__ == "__main__":
    n, m = list(map(int, input().strip().split(' ')))
    athletes = []
    for _ in range(n):
        athletes.append(list(map(int, input().strip().split(' '))))
    k = int(input())
    athletes.sort(key=lambda x:x[k])
    for athlete in athletes:
        print(' '.join(map(str, athlete)))
