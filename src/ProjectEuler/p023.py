#!/usr/bin/python
#coding: UTF-8
"""
@author: CaiKnife

Non-abundant sums
Problem 23
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""

from euler import dd

MAX_NUMBER = 28124
abundant_numbers = [n for n in range(1, MAX_NUMBER) if dd(n) > n]
abundant_dict = dict.fromkeys(abundant_numbers, True)

total = 0
for n in range(1, MAX_NUMBER):
    sum_of_abundants = False
    for a in abundant_numbers:
        if a > n:
            break
        if abundant_dict.get(n-a):
            sum_of_abundants = True
            break
    if not sum_of_abundants:
        total += n

print total

