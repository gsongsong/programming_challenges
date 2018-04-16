# https://www.hackerrank.com/challenges/zipped/problem

if __name__ == "__main__":
    n, x = list(map(int, input().strip().split(' ')))
    scores = []
    for _ in range(x):
        scores.append(list(map(float, input().strip().split(' '))))
    for z in zip(*scores):
        print('{0:.1f}'.format(sum(z) / len(z)))
