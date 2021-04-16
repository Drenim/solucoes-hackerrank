#!/bin/python3

import sys


def fruit_hits(start_h, end_h, fruit_tree, fruit_list):
    count = 0
    for a in fruit_list:
        if start_h <= a + fruit_tree <= end_h:
            count += 1
    return count


s, t = input().strip().split(' ')
s, t = [int(s), int(t)]
a, b = input().strip().split(' ')
a, b = [int(a), int(b)]
m, n = input().strip().split(' ')
m, n = [int(m), int(n)]
apple = [int(apple_temp) for apple_temp in input().strip().split(' ')]
orange = [int(orange_temp) for orange_temp in input().strip().split(' ')]

print(str(fruit_hits(s, t, a, apple)))
print(str(fruit_hits(s, t, b, orange)))
