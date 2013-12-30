#!/usr/bin/python
#coding: UTF-8
"""
@author: CaiKnife

Circular primes
Problem 35
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
"""

from euler import get_digits, is_prime


def is_circular(n):
    digits = [str(x) for x in get_digits(n)]
    for d in range(len(digits)):
        r = int("".join(digits[d:] + digits[0:d]))
        if not is_prime(r):
            return False
    return True

circulars = [2]
for x in range(3, 1000000, 2):
    if is_circular(x):
        circulars.append(x)

print len(circulars)
