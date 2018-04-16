#!/bin/python3

# https://www.hackerrank.com/challenges/runningtime/problem

import sys

def insertionSort1(arr, curr_idx):
    # Re-use (slightly modified) Insertion Sort - Part 1
    num = arr[curr_idx]
    shift = 0
    # i from len-1 to 1
    for i in range(curr_idx, 0, -1):
        # idx from curr_idx-1 to 0
        idx = i - 1
        curr_num = arr[idx]
        if num < curr_num:
            arr[idx + 1] = curr_num
            if idx == 0:
                arr[idx] = num
            shift += 1
        else:
            arr[idx+1] = num
            break
    return shift

def insertionSort2(arr):
    # Complete this function
    shift = 0
    for idx in range(1, len(arr)):
        shift += insertionSort1(arr, idx)
    return shift

def runningTime(arr):
    # Complete this function
    return insertionSort2(arr)

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    result = runningTime(arr)
    print(result)
