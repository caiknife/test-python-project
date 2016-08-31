#!/usr/bin/python
# coding: UTF-8
"""
@author: CaiKnife

Pandigital prime
Problem 41
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
"""

# 8位数和9位数的pandigital肯定不是质数，因为能被3整除
from euler import is_prime
from itertools import permutations

all_digits = [int("".join(str(i) for i in p)) for p in permutations(range(1, 8))]
print max([n for n in all_digits if is_prime(n)])
