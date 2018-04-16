# https://www.hackerrank.com/challenges/iterables-and-iterators/problem

import itertools

if __name__ == "__main__":
    N = int(input())
    letters = input().strip().split(' ')
    K = int(input())
    occurence = 0
    total = 0
    for c in itertools.combinations(letters, K):
        total += 1
        if 'a' in c:
            occurence += 1
    print(occurence / total)
