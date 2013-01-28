#!/usr/bin/python
#coding: UTF-8
"""
@author: CaiKnife

Power digit sum
Problem 16
215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 21000?
"""

NUMBER = 2**1000

print NUMBER
print sum([int(x) for x in str(NUMBER)])