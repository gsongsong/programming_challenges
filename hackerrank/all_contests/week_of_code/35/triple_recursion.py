#!/bin/python3

# https://www.hackerrank.com/contests/w35/challenges/triple-recursion

import sys

def print_matrix(matrix):
    for row in matrix:
        print(' '.join(map(str, row)))

def tripleRecursion(n, m, k):
    # Complete this function
    matrix = []
    for i in range(n):
        matrix.append([0] * n)
        for j in range(n):
            if i < j:
                matrix[i][j] = matrix[i][j - 1] - 1
            elif i > j:
                matrix[i][j] = matrix[i - 1][j] - 1
            else:
                matrix[i][i] = m + i * k
    print_matrix(matrix)

if __name__ == "__main__":
    n, m, k = input().strip().split(' ')
    n, m, k = [int(n), int(m), int(k)]
    tripleRecursion(n, m, k)
