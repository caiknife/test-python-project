#!/usr/bin/python
#coding: UTF-8
"""
@author: CaiKnife

Digit factorials
Problem 34
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
"""

from euler import factorial, get_digits

fact = (1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880)

def is_curious(n):
    return sum([factorial(x) for x in get_digits(n)]) == n

print sum([x for x in range(3, 100000) if is_curious(x)])