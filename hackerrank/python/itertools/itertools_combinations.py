# https://www.hackerrank.com/challenges/itertools-combinations/problem

import itertools

if __name__ == "__main__":
    line = input().strip().split(' ')
    word = list(line[0])
    word.sort()
    n = int(line[1])
    for i in range(1, n + 1):
        for c in itertools.combinations(word, i):
            print(''.join(c))
