#!/usr/bin/python
#coding: UTF-8
"""
@author: CaiKnife

Largest palindrome product
Problem 4
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

bound = range(999, 100, -1)
results = [x*y for x in bound for y in bound if str(x*y) == str(x*y)[::-1]]
print max(results)
