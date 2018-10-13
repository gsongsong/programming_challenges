# https://www.hackerrank.com/challenges/contacts

import os
import sys

#
# Complete the contacts function below.
#
def contacts(queries):
    #
    # Write your code here.
    #
    result = []
    root = {'tot': 0}
    for q in queries:
        command = q[0]
        if command == 'add':
            add(root, q[1])
        elif command == 'find':
            result.append(find(root, q[1]))
    return result

def add(trie, word):
    curr = trie
    for c in word:
        if c not in curr:
            curr[c] = {'tot': 0}
        curr['tot'] += 1
        curr = curr[c]
    if curr != trie:
        curr['tot'] += 1

def find(trie, word):
    curr = trie
    for c in word:
        if c not in curr:
            return 0
        curr = curr[c]
    return curr['tot']

if __name__ == '__main__':
    queries_rows = int(input())
    queries = []
    for _ in range(queries_rows):
        queries.append(input().rstrip().split())
    result = contacts(queries)
    print('\n'.join(map(str, result)))
    print('\n')

