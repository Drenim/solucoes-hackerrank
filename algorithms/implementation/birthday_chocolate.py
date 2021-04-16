#!/bin/python3


def solve(n, s, d, m):
    counter = 0

    for i in range(0, n):
        slice_sum = sum(s[i:i+m])
        if slice_sum == d:
            counter += 1

    return counter


n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
d, m = input().strip().split(' ')
d, m = [int(d), int(m)]
result = solve(n, s, d, m)
print(result)
