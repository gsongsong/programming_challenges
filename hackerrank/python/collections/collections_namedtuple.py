# https://www.hackerrank.com/challenges/py-collections-namedtuple/problem
if __name__ == "__main__":
    n, idx_marks, total = int(input()), input().strip().split().index('MARKS'), 0
    total = sum([int(input().strip().split()[idx_marks]) for i in range(n)])
    print(total / n)
