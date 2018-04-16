# https://www.hackerrank.com/challenges/py-set-mutations/problem

if __name__ == "__main__":
    lenA = int(input())
    a = set(map(int, input().strip().split(' ')))
    n = int(input())
    for _ in range(n):
        line = input().strip().split(' ')
        com = line[0]
        if com == 'update':
            a |= set(map(int, input().strip().split(' ')))
        if com == 'intersection_update':
            a &= set(map(int, input().strip().split(' ')))
        if com == 'symmetric_difference_update':
            a ^= set(map(int, input().strip().split(' ')))
        if com == 'difference_update':
            a -= set(map(int, input().strip().split(' ')))
    print(sum(a))
