# https://www.hackerrank.com/challenges/dynamic-array/problem

#!/bin/python3

import os
import sys

#
# Complete the dynamicArray function below.
#
def dynamicArray(n, queries):
    #
    # Write your code here.
    #
    l = [[] for _ in range(n)]
    last_answer = 0
    for query in queries:
        seq_idx = (query[1] ^ last_answer) % n
        if query[0] == 1:
            l[seq_idx].append(query[2])
        elif query[0] == 2:
            last_answer = l[seq_idx][query[2] % len(l[seq_idx])]
            print(last_answer)

if __name__ == '__main__':
    nq = input().split()
    n = int(nq[0])
    q = int(nq[1])
    queries = []
    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))
    dynamicArray(n, queries)
