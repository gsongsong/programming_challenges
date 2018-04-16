# https://www.hackerrank.com/challenges/py-collections-deque/problem

import collections

if __name__ == "__main__":
    dq = collections.deque()
    n = int(input())
    for _ in range(n):
        line = input().strip().split(' ')
        command = line[0]
        if command == 'append':
            dq.append(int(line[1]))
        elif command == 'appendleft':
            dq.appendleft(int(line[1]))
        elif command == 'pop':
            dq.pop()
        elif command == 'popleft':
            dq.popleft()
    print(' '.join(map(str, dq)))
