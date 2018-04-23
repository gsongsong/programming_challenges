# https://www.hackerrank.com/challenges/queue-using-two-stacks/problem

if __name__ == '__main__':
    tail_last = []
    head_last = []
    n = int(input())
    for _ in range(n):
        line = list(map(int, input().split()))
        if line[0] == 1:
            tail_last.append(line[1])
        else:
            if not head_last:
                while tail_last:
                    head_last.append(tail_last.pop())
            if line[0] == 2:
                head_last.pop()
            elif line[0] == 3:
                print(head_last[-1])
