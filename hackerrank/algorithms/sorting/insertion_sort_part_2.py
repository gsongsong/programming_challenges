#!/bin/python3

# https://www.hackerrank.com/challenges/insertionsort2/problem

import sys

def print_arr(arr):
    print(' '.join(map(str, arr)))

def insertionSort1(arr, curr_idx):
    # Re-use (slightly modified) Insertion Sort - Part 1
    num = arr[curr_idx]
    # i from len-1 to 1
    for i in range(curr_idx, 0, -1):
        # idx from curr_idx-1 to 0
        idx = i - 1
        curr_num = arr[idx]
        if num < curr_num:
            arr[idx + 1] = curr_num
            if idx == 0:
                arr[idx] = num
        else:
            arr[idx+1] = num
            break
    print_arr(arr)

def insertionSort2(n, arr):
    # Complete this function
    for idx in range(1, len(arr)):
        insertionSort1(arr, idx)

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    insertionSort2(n, arr)
