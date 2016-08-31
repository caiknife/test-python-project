#!/usr/bin/python
# coding: UTF-8
"""
@author: CaiKnife

Consecutive prime sum
Problem 50
The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?
"""
from euler import is_prime, prime_generator

g = prime_generator()
primes, n = [], 0

while True:
    i = g.next()
    primes.append(i)
    n += i
    if n > 1000000:
        break

n -= i

for p in primes:
    n -= p
    if is_prime(n):
        break

print n
