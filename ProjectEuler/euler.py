#!/usr/bin/python
#coding: UTF-8
"""
@author: CaiKnife

common functions for project euler
"""
import math
from functools import wraps

def factor(num):
    """
    For Problem 1
    """
    if not num % 3 or not num % 5:
        return True
    return False


def cache(func):
    """
    cache decorator
    用来装饰递归调用的函数
    """
    caches = {}
    @wraps(func)
    def wrap(*args):
        if args not in caches:
            caches[args] = func(*args)
        return caches[args]
    return wrap

@cache
def fib(num):
    """
    For Problem 2
    """
    if num == 1:
        return 1
    elif num == 2:
        return 2
    return fib(num-1) + fib(num-2)

@cache
def gcd(a, b):
    """
    For Problem 5
    """
    if a == 0:
        return b
    else:
        return gcd(b%a, a)

def is_prime(num):
    """
    For Problem 7
    """
    if num <= 1:
        return False
    elif num == 2:
        return True
    else:
        root = math.sqrt(num)
        i = 3
        while i <= root:
            if num % i == 0:
                return False
            i += 2
        return True
        
def traingle_number(n):
    """
    For Problem 12
    """
    return n*(n+1)/2

def count_divisors(number):
    return len(divisors(number))

def collatz_seq(n):
    """
    For Problem 14
    """
    r = []
    while n>1:
        r.append(n)
        if n % 2 == 0:
            n = n/2
        else:
            n = 3*n + 1
    r.append(n)
    return r

def factorial(n):
    """
    For Problem 20
    """
    r = 1
    while n > 1:
        r *= n
        n = n - 1
    return r

def divisors(n):
    """
    For Problem 21
    """
    if n == 0:
        return []

    r, i, root = [], 1, math.sqrt(n)
    while i < root:
        if n % i == 0:
            r.extend([i, n/i])
        i += 1
    # perfect square
    if n % root == 0:
        r.append(int(root))
    r.sort()
    return r

def dd(n):
    r = divisors(n)
    return sum(r[:-1])
