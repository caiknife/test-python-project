#!/usr/bin/python
# coding: UTF-8
"""
@author: CaiKnife

Distinct primes factors
Problem 47
The first two consecutive numbers to have two distinct prime factors are:

14 = 2  7
15 = 3  5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2²  7  23
645 = 3  5  43
646 = 2  17  19.

Find the first four consecutive integers to have four distinct primes factors. What is the first of these numbers?
"""
from euler import prime_factors, prime_generator, is_prime
# TOO SLOW!!!!
#
# def distinct_prime_factors(n):
#     try:
#         return set(prime_factors(n))
#     except:
#         return set([])

# g = prime_generator()

# r = []
# for i in range(1000, 100000):
#     if len(distinct_prime_factors(i)) == 4:
#         r.append(i)

# print (r[i:i+4] for i, n in enumerate(r) if r[i:i+search] == range(n, n+4)).next()[0]


import math


def factorize(n):
    if n < 1:
        raise ValueError('fact() argument should be >= 1')
    if n == 1:
        return []  # special case
    res = []
    # iterate over all even numbers first.
    while n % 2 == 0:
        res.append(2)
        n //= 2
    # try odd numbers up to sqrt(n)
    limit = math.sqrt(n + 1)
    i = 3
    while i <= limit:
        if n % i == 0:
            res.append(i)
            n //= i
            limit = math.sqrt(n + i)
        else:
            i += 2
    if n != 1:
        res.append(n)
    return res


def distinct_prime_factors(n):
    return set(factorize(n))


def main():
    chain = []
    search = 4
    for n in range(1, 1000000):
        if len(distinct_prime_factors(n)) == search:
            chain.append(n)
    print(chain[i:i + search] for i, n in enumerate(chain) if
          chain[i:i + search] == range(n, n + search)).next()[0]


if __name__ == "__main__":
    main()
