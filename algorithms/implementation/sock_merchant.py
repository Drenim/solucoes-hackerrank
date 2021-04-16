#!/bin/python3
from collections import Counter


def sockMerchant(n, ar):
    counter = Counter(ar)
    n_pairs = 0

    for quant in counter.values():
        n_pairs += (quant - (quant % 2)) // 2

    return n_pairs


n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = sockMerchant(n, ar)
print(result)
