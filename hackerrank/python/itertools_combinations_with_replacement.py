# https://www.hackerrank.com/challenges/itertools-combinations-with-replacement/problem

import itertools

if __name__ == "__main__":
    line = input().strip().split(' ')
    word = sorted(list(line[0]))
    n = int(line[1])
    for c in itertools.combinations_with_replacement(word, n):
        print(''.join(c))
