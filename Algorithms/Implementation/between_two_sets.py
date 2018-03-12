#!/bin/python3


def getTotalX(a, b):
    limite_sup = min(b)
    limite_inferior = max(a)

    counter = 0
    for i in range(limite_inferior, limite_sup + 1):
        is_between = True
        for elem_a in a:
            if i % elem_a != 0:
                is_between = False
                break
        for elem_b in b:
            if elem_b % i != 0:
                is_between = False
                break
        if is_between:
            counter += 1

    return counter


if __name__ == "__main__":
    n, m = input().strip().split(' ')
    n, m = [int(n), int(m)]
    a = list(map(int, input().strip().split(' ')))
    b = list(map(int, input().strip().split(' ')))
    total = getTotalX(a, b)
    print(total)
