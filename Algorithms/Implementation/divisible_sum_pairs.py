#!/bin/python3


def divisibleSumPairs(n, k, ar):
    counter = 0

    for j, aj in enumerate(ar[1:]):
        for i, ai in enumerate(ar[:j+1]):
            if (ai + aj) % k == 0:
                counter += 1

    return counter


n, k = input().strip().split(' ')
n, k = [int(n), int(k)]
ar = list(map(int, input().strip().split(' ')))
result = divisibleSumPairs(n, k, ar)
print(result)
