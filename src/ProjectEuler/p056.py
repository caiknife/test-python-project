#!/usr/bin/python
#coding: UTF-8
"""
@author: CaiKnife

Powerful digit sum
Problem 56
A googol (10100) is a massive number: one followed by one-hundred zeros; 100100 is almost unimaginably large: one followed by two-hundred zeros. Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, ab, where a, b  100, what is the maximum digital sum?
"""

from euler import get_digits

m = 0
for a in xrange(1, 100):
    for b in xrange(1, 100):
        digit_sum = sum(get_digits(a**b))
        if m < digit_sum:
            m = digit_sum

print m