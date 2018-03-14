#!/bin/python3


def solve(k, arr, b):
    sum_arr = 0

    for i, elem in enumerate(arr):
        if i != k:
            sum_arr += int(elem)

    if b == sum_arr / 2:
        return 'Bon Appetit'
    else:
        return int(b - sum_arr / 2)


n, k = input().strip().split(' ')
n, k = int(n), int(k)
arr = input().strip().split(' ')
b = int(input().strip())
print(solve(k, arr, b))
