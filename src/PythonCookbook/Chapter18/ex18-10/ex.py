#!/usr/bin/python
# coding: UTF-8
"""
Created on 2012-11-24
计算素数
@author: CaiKnife
"""

import itertools


def eratosthenes():
    'Eratosthenes筛选法生成素数序列'
    D = {}
    for q in itertools.count(2):
        p = D.pop(q, None)
        if p is None:
            yield q
            D[q * q] = q
        else:
            x = p + q
            while x in D:
                x += p
            D[x] = p


def primes_less_than(N):
    primes = [x for x in (2, 3, 5, 7, 11, 13) if x < N]
    if N <= 17:
        return primes

    candidates = [x for x in xrange((N - 2) | 1, 15, -2) if
                  x % 3 and x % 5 and x % 7 and x % 11 and x % 13]
    top = int(N ** 0.5)
    while (top + 1) * (top + 1) <= N:
        top += 1
    while True:
        p = candidates.pop()
        primes.append(p)
        if p > top:
            break
        candidates = filter(p.__rmod__, candidates)

    candidates.reverse()
    primes.extend(candidates)
    return primes
