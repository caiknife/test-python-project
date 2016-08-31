#!/usr/bin/python
# coding: UTF-8
"""
@author: CaiKnife

Quadratic primes
Problem 27
Euler published the remarkable quadratic formula:

n² + n + 41

It turns out that the formula will produce 40 primes for the consecutive values n = 0 to 39. However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, and certainly when n = 41, 41² + 41 + 41 is clearly divisible by 41.

Using computers, the incredible formula  n²  79n + 1601 was discovered, which produces 80 primes for the consecutive values n = 0 to 79. The product of the coefficients, 79 and 1601, is 126479.

Considering quadratics of the form:

n² + an + b, where |a|  1000 and |b|  1000

where |n| is the modulus/absolute value of n
e.g. |11| = 11 and |4| = 4
Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n = 0.
"""

from euler import is_prime
from itertools import product


def num_primes(func):
    n = 0
    while True:
        r = func(n)
        if not is_prime(r):
            break
        n += 1
    return n


max_pair = (0, 0, 0)

for a, b in product(range(-999, 1000), range(-999, 1000)):
    func = lambda n: n ** 2 + a * n + b
    num = num_primes(func)
    if num > max_pair[2]:
        max_pair = (a, b, num)

print max_pair[0] * max_pair[1]
