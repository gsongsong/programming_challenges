# https://www.hackerrank.com/challenges/nested-list/problem

if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        arr = [name, score]
        students.append([name, score])
    students.sort(key = lambda x: x[1])
    score_1st = students[0][1]
    score_2nd = None
    students_2nd = []
    for student in students[1:]:
        if student[1] > score_1st and not score_2nd:
            score_2nd = student[1]
            students_2nd.append(student[0])
            continue
        if student[1] == score_2nd:
            students_2nd.append(student[0])
    students_2nd.sort()
    for student in students_2nd:
        print(student)
