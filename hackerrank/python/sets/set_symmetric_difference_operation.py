# https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem

if __name__ == "__main__":
    n = input()
    arr = map(int, input().strip().split(' '))
    n = input()
    brr = map(int, input().strip().split(' '))
    symm_diff = list(set(arr) ^ set(brr))
    symm_diff.sort()
    for elem in symm_diff:
        print(elem)
