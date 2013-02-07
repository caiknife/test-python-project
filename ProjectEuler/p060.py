#!/usr/bin/python
#coding: UTF-8
"""
@author: CaiKnife

Prime pair sets
Problem 60
The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating them in any order the result will always be prime. For example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four primes, 792, represents the lowest sum for a set of four primes with this property.

Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.
"""
from euler import is_prime, make_primes
from itertools import combinations

def remarkable_prime(a, b):
    return is_prime(int(str(a)+str(b))) and is_prime(int(str(b)+str(a)))

def a_set_of_five_primes(sets):
    for p in combinations(sets, 2):
        if not remarkable_prime(p[0], p[1]):
            return False
    return True

def main():
    primes = make_primes(10000)
    primes.remove(2)
    all_five_primes = combinations(primes, 5)
    for p in all_five_primes:
        if a_set_of_five_primes(p):
            print sum(p)
            return

if __name__ == '__main__':
    main()