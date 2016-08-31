#!/usr/bin/python
# coding: UTF-8
"""
@author: CaiKnife

10001st prime
Problem 7
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""

from euler import is_prime


def number_generator():
    i = 3
    while True:
        yield i
        i += 2


def list_prime(num=None):
    i = 1
    gen = number_generator()
    while True:
        n = gen.next()
        if is_prime(n):
            i += 1
        if i >= num:
            return i, n


print list_prime(10001)
