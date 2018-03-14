#!/bin/python3


def migratoryBirds(n, ar):
    types = [0] * 6

    for elem in ar:
        types[elem] += 1

    most_common = 0
    for i, elem in enumerate(types):
        if elem > types[most_common]:
            most_common = i

    return most_common


n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = migratoryBirds(n, ar)
print(result)
