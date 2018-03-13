#!/bin/python3


def solve(grades):
    new_grades = []

    for i in grades:
        if i >= 38:
            next_multiple = i + (5 - (i % 5))
            if next_multiple - i < 3:
                i = next_multiple
        new_grades.append(i)

    return new_grades


n = int(input().strip())
grades = []
grades_i = 0
for grades_i in range(n):
    grades_t = int(input().strip())
    grades.append(grades_t)
result = solve(grades)
print("\n".join(map(str, result)))
