# https://www.hackerrank.com/challenges/python-mutations/problem

def mutate_string(string, position, character):
    str_list = list(string)
    str_list[position] = character
    return ''.join(str_list)
