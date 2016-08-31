#!/usr/bin/python
# coding: UTF-8
"""
@author: CaiKnife

Special Pythagorean triplet
Problem 9
A Pythagorean triplet is a set of three natural numbers, a  b  c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

a = b = c = 1

data = [(a, b, 1000 - a - b) for a in range(500) for b in range(a) if
        a ** 2 + b ** 2 == (1000 - a - b) ** 2]
print data[0][0] * data[0][1] * data[0][2]
