#!/usr/bin/python
# coding: UTF-8
"""
@author: CaiKnife

Multiples of 3 and 5
Problem 1
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

from euler import factor

bound = range(3, 1000)
print sum([x for x in bound if factor(x)])
