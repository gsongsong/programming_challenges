# https://www.hackerrank.com/challenges/no-idea/problem

if __name__ == "__main__":
    n, m = input().strip().split(' ')
    arr = input().strip().split(' ')
    a = set(input().strip().split(' '))
    b = set(input().strip().split(' '))
    happiness = 0
    for elem in arr:
        if elem in a:
            happiness += 1
        elif elem in b:
            happiness -= 1
    print(happiness)
