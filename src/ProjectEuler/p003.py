#!/usr/bin/python
# coding: UTF-8
"""
@author: CaiKnife

Largest prime factor
Problem 3
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

number = 600851475143
i = 2

while i != number:
    if not number % i:
        number = number / i
    else:
        i += 1

print number
