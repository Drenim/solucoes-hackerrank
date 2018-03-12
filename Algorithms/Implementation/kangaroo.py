#!/bin/python3


def will_match(x1, v1, x2, v2):
    if v2 - v1 == 0:
        return False

    solution = (x1 - x2) / (v2 - v1)

    if solution.is_integer() and solution >= 0:
        return True
    return False


_x1, _v1, _x2, _v2 = input().strip().split(' ')
_x1, _v1, _x2, _v2 = [int(_x1), int(_v1), int(_x2), int(_v2)]

if (will_match(_x1, _v1, _x2, _v2)):
    print("YES")
else:
    print("NO")
