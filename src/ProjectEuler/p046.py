#!/usr/bin/python
#coding: UTF-8
"""
@author: CaiKnife

Goldbach's other conjecture
Problem 46
It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

9 = 7 + 212
15 = 7 + 222
21 = 3 + 232
25 = 7 + 232
27 = 19 + 222
33 = 31 + 212

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
"""
from euler import is_prime, make_primes
from itertools import product

PRIMES = make_primes(10000)


def is_conjecture(n):
    if is_prime(n):
        return False
    if not n % 2:
        return False
    c = product(PRIMES, [2*i**2 for i in range(1, 100)])
    for p in c:
        if n == p[0] + p[1]:
            return True
    return False


for i in range(9, 10000):
    if not is_prime(i) and i % 2 and not is_conjecture(i):
        print i
