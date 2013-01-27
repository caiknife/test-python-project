#!/usr/bin/python
#coding: UTF-8
"""
@author: CaiKnife

Smallest multiple
Problem 5
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

from euler import gcd

answer = 1
for i in range(1, 21):
    answer *= i / gcd(answer, i)

print answer