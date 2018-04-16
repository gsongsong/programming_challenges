# https://www.hackerrank.com/challenges/find-a-string/problem

def count_substring(string, sub_string):
    num_substr = 0
    for i in range(len(string)):
        if string[i:].startswith(sub_string):
            num_substr += 1
    return num_substr
