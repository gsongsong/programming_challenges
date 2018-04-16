#!/bin/python3

# https://www.hackerrank.com/challenges/cavity-map/problem

import sys

def cavityMap(grid):
    # Complete this function
    grid_list = [list(map(int, row)) for row in grid]
    n = len(grid_list)
    cavities = []
    for i in range(1, n - 1):
        for j in range(1, n - 1):
            if grid_list[i][j] > grid_list[i][j-1] and \
               grid_list[i][j] > grid_list[i][j+1] and \
               grid_list[i][j] > grid_list[i-1][j] and \
               grid_list[i][j] > grid_list[i+1][j]:
                cavities.append((i, j))
    for cavity in cavities:
        grid_list[cavity[0]][cavity[1]] = 'X'
    return [''.join(map(str, row)) for row in grid_list]

if __name__ == "__main__":
    n = int(input().strip())
    grid = []
    grid_i = 0
    for grid_i in range(n):
       grid_t = str(input().strip())
       grid.append(grid_t)
    result = cavityMap(grid)
    print ("\n".join(map(str, result)))
