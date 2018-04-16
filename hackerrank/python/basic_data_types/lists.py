# https://www.hackerrank.com/challenges/python-lists/problem

if __name__ == '__main__':
    N = int(input())
    l = []
    for _ in range(N):
        line = input().strip().split(' ')
        command = line[0]
        if command == 'insert':
            l.insert(int(line[1]), int(line[2]))
        elif command == 'print':
            print(l)
        elif command == 'remove':
            l.remove(int(line[1]))
        elif command == 'append':
            l.append(int(line[1]))
        elif command == 'sort':
            l.sort()
        elif command == 'pop':
            l.pop()
        elif command == 'reverse':
            l.reverse()
