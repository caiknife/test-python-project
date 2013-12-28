#!/usr/bin/python
#coding: UTF-8
"""
@author: CaiKnife

Truncatable primes
Problem 37
The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""

from euler import is_prime, get_digits

def truncatable_from_left(n):
    d = get_digits(n, integer=False)
    m = [is_prime(int("".join(d[i:]))) for i in range(len(d))]
    return reduce(lambda x, y: x and y, m)

def truncatable_form_right(n):
    d = get_digits(n, integer=False)
    m = [is_prime(int("".join(d[:i]))) for i in range(1, len(d))] + [is_prime(n)]
    return reduce(lambda x, y: x and y, m)

def is_curious(n):
    return truncatable_from_left(n) and truncatable_form_right(n)

data = []
n = 11
while True:
    if is_curious(n):
        data.append(n)
    if len(data) == 11:
        break
    n += 2

print sum(data)
