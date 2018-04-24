# Given an integer array, print the second largest value
#
# ex.
# Input: [10, 5, 4, 3, -1]
# Output: 5
# Input: [3, 3, 3]
# Output: Does not exist.

if __name__ == '__main__':
    arr = list(map(int, input().split()))
    max_1 = arr[0]
    max_2 = None
    for elem in arr[1:]:
        if elem > max_1:
            max_2 = max_1
            max_1 = elem
            continue
        if elem == max_1:
            continue
        if elem > max_2:
            max_2 = elem
    print(max_2)
