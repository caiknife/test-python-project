#!/usr/bin/python
# coding: UTF-8
"""
@author: CaiKnife

Pandigital products
Problem 32
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39  186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
"""
from euler import is_pandigital

pan_digits = []

for a in range(1, 5000):
    for b in range(1, 100):
        c = a * b
        if is_pandigital(a, b, c, length=9) and c not in pan_digits:
            pan_digits.append(c)

print sum(pan_digits)
