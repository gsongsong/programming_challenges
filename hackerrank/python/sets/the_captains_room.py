# https://www.hackerrank.com/challenges/py-the-captains-room/problem

if __name__ == "__main__":
    k = int(input())
    arr = list(map(int, input().strip().split(' ')))
    exist = set()
    duplicates = set()
    for elem in arr:
        if elem in exist:
            duplicates.add(elem)
            continue
        exist.add(elem)
    print(list(exist - duplicates)[0])
