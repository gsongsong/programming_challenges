# https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem

if __name__ == "__main__":
    n = int(input())
    s = set(map(int, input().strip().split(' ')))
    N = int(input())
    for _ in range(N):
        line = input().strip().split(' ')
        command = line[0]
        if command == 'pop':
            s.pop()
        if command == 'remove':
            s.remove(int(line[1]))
        if command == 'discard':
            s.discard(int(line[1]))
    print(sum(s))
