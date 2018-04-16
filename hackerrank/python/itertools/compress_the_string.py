# https://www.hackerrank.com/challenges/compress-the-string/problem

import itertools

if __name__ == "__main__":
    string = input().strip()
    for k, g in itertools.groupby(string):
        print('({0}, {1})'.format(len(list(g)), k), end=' ')
