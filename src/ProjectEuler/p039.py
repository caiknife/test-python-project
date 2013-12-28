#!/usr/bin/python
#coding: UTF-8
"""
@author: CaiKnife

Integer right triangles
Problem 39
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p  1000, is the number of solutions maximised?
"""
from collections import defaultdict

def solutions(p):
    s = []
    for a in range(1, p/3):
        for b in range(a, (p-a)/2):
            c = p - a - b
            if a**2 + b**2 == c**2:
                s.append((a, b, c))
    return s

ma = ms = 0
for p in range(12, 1001, 2):
    s = len(solutions(p))
    if ms < s:
        ma, ms = p, s

print ma