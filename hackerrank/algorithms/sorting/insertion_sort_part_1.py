#!/bin/python3

# https://www.hackerrank.com/challenges/insertionsort1/problem

import sys

def print_arr(arr):
    print(' '.join(map(str, arr)))

def insertionSort1(n, arr):
    # Complete this function
    num = arr[-1]
    # i from len-1 to 1
    for i in range(len(arr) - 1, 0, -1):
        # idx from len-2 (second last one) to 0
        idx = i - 1
        curr_num = arr[idx]
        if num < curr_num:
            arr[idx + 1] = curr_num
            print_arr(arr)
            if idx == 0:
                arr[idx] = num
                print_arr(arr)
        else:
            arr[idx+1] = num
            print_arr(arr)
            break

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    insertionSort1(n, arr)
