#!/usr/bin/python
# coding: UTF-8
"""
@author: CaiKnife

Summation of primes
Problem 10
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

from euler import is_prime

MAX_NUMBER = 2000000
data = [i for i in range(1, MAX_NUMBER, 2) if is_prime(i)]
# 上面这个循环的结果里少了个2，最后的结果要加上2
print sum(data) + 2
