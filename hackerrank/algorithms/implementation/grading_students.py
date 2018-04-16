#!/bin/python3

# https://www.hackerrank.com/challenges/grading/problem

import sys

def solve(grades):
    # Complete this function
    grades_rounded_up = []
    for grade in grades:
        if grade >= 38:
            deficit = 5 - (grade % 5)
            if deficit < 3:
                grade += deficit
        grades_rounded_up.append(grade)
    return grades_rounded_up

n = int(input().strip())
grades = []
grades_i = 0
for grades_i in range(n):
   grades_t = int(input().strip())
   grades.append(grades_t)
result = solve(grades)
print ("\n".join(map(str, result)))
