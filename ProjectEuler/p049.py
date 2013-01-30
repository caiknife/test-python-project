#!/usr/bin/python
#coding: UTF-8
"""
@author: CaiKnife

Prime permutations
Problem 49
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
"""

from itertools import permutations
from euler import make_primes, is_prime, get_digits

def to_tuple(n):
    return tuple(str(n))

primes = [p for p in make_primes(10000) if len(str(p))==4]
primes = [p for p in primes if is_prime(p+3330) and len(str(p+3330))==4 and is_prime(p+6660) and len(str(p+6660))==4] 
for p in primes:
    per = permutations(to_tuple(p))
    if to_tuple(p+3330) in  per and to_tuple(p+6660) in per:
        print p, p+3330, p+6660


