#!/usr/bin/python
# coding: UTF-8
"""
@author: CaiKnife

Factorial digit sum
Problem 20
n! means n  (n  1)  ...  3  2  1

For example, 10! = 10  9  ...  3  2  1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""

from euler import factorial

print sum([int(x) for x in str(factorial(100))])
