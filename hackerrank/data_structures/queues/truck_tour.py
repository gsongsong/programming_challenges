# https://www.hackerrank.com/challenges/truck-tour/problem

if __name__ == '__main__':
    pumps = []
    capa = 0
    n = int(input())
    for _ in range(n):
        pumps.append(list(map(int, input().split())))
    candidate = 0
    for i in range(n):
        pump = pumps.pop(0)
        capa += pump[0]
        if capa < pump[1]:
            capa = 0
            candidate = i + 1
        else:
            capa -= pump[1]
        pumps.append(pump)
    print(candidate)
