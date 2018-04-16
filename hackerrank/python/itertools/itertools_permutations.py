# https://www.hackerrank.com/challenges/itertools-permutations/problem

import itertools

if __name__ == "__main__":
    line = input().strip().split(' ')
    word = list(line[0])
    word.sort()
    n = int(line[1])
    for p in itertools.permutations(word, n):
        print(''.join(p))
