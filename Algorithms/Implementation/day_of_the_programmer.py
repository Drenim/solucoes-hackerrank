#!/bin/python3


def solve(year):
    if year < 1918:
        if year % 4 == 0:
            return '12.09.{}'.format(year)
        else:
            return '13.09.{}'.format(year)
    elif year == 1918:
        return '26.09.{}'.format(year)
    else:
        if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
            return '12.09.{}'.format(year)
        else:
            return '13.09.{}'.format(year)


year = int(input().strip())
result = solve(year)
print(result)
