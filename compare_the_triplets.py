#!/bin/python3

import sys


a0,a1,a2 = input().strip().split(' ')
a_l = [int(a0),int(a1),int(a2)]
b0,b1,b2 = input().strip().split(' ')
b_l = [int(b0),int(b1),int(b2)]

a_p = 0
b_p = 0
for ai, bi in zip(a_l, b_l):
    if ai > bi:
        a_p+= 1
    elif bi > ai:
        b_p += 1

print("{} {}".format(a_p, b_p))
