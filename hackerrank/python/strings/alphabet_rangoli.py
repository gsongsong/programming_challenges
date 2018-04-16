# https://www.hackerrank.com/challenges/alphabet-rangoli/problem

def print_row(n, size):
    row = []
    for i in range(size, size - n, - 1):
        row.append(chr(i + ord('a') -1))
    for i in range(size - n + 2, size + 1):
        row.append(chr(i + ord('a') - 1))
    print('-'.join(row).center(4 * size- 3, '-'))

def print_rangoli(size):
    # your code goes here
    for i in range(1, size + 1):
        print_row(i, size)
    for i in range(size - 1, 0, -1):
        print_row(i, size)
