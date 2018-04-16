# https://codejam.withgoogle.com/2018/challenges/00000000000000cb/dashboard/00000000000079cb

# Even-indexed and odd-indexed items are sorted separately
def trouble_sort(arr):
    arr_even, arr_odd = sorted(arr[0::2]), sorted(arr[1::2])
    # print(arr_even)
    # print(arr_odd)
    for i in range(len(arr_odd)):
        #                 arr_odd[i]
        # arr_even[i]            arr_even[i + 1]
        if arr_even[i] > arr_odd[i]:
            return 2 * i
        if i + 1 < len(arr_even) and arr_odd[i] > arr_even[i + 1]:
            return 2 * i + 1
    return 'OK'

if __name__ == '__main__':
    n = int(input())
    for i in range(1, n + 1):
        l = int(input())
        arr = list(map(int, input().strip().split()))
        print('Case #{0}: {1}'.format(i, trouble_sort(arr)))
