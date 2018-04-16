# https://www.hackerrank.com/challenges/piling-up/problem

import collections

def stack():
    dq = collections.deque(map(int, input().strip().split(' ')))
    cube_last = None
    while dq:
        if dq[0] > dq[-1]:
            cube = dq.popleft()
        else:
            cube = dq.pop()
        if not cube_last:
            cube_last = cube
            continue
        if cube > cube_last:
            print('No')
            return
    print('Yes')

if __name__ == "__main__":
    t = int(input())
    for ti in range(t):
        n = int(input())
        stack()
