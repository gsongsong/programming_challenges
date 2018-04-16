# https://www.hackerrank.com/challenges/map-and-lambda-expression/problem

cube = lambda x: x ** 3# complete the lambda function

def fibonacci(n):
    # return a list of fibonacci numbers
    if n == 0:
        return []
    if n == 1:
        return [0]
    fibb = [0, 1]
    for i in range(2, n):
        fibb.append(fibb[i - 1] + fibb[i - 2])
    return fibb
