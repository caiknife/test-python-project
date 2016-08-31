#!/usr/bin/python
# coding: UTF-8
"""
@author: CaiKnife

Lattice paths
Problem 15
Starting in the top left corner of a 22 grid, there are 6 routes (without backtracking) to the bottom right corner.


How many routes are there through a 2020 grid?
"""


def fact(n):
    f = 1
    for x in range(1, n + 1):
        f *= x
    return f


print fact(40) / fact(20) / fact(20)
