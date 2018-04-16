# https://www.hackerrank.com/challenges/exceptions/problem

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        a, b = input().strip().split(' ')
        try:
            print(int(a) // int(b))
        except ValueError as e:
            print('Error Code:', e)
        except ZeroDivisionError as e:
            print('Error Code:', e)
