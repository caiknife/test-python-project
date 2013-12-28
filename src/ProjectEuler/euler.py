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
    if (num != 2 and num % 2 == 0) or (num != 3 and num % 3 == 0):
        return False
    if num > 1 and count_divisors(num) == 2:
        return True
    else:
        return False
    # if num <= 1:
    #     return False
    # if num == 2:
    #     return True
    # else:
    #     root = math.sqrt(num)
    #     i = 3
    #     while i <= root:
    #         if num % i == 0:
    #             return False
    #         i += 2
    #     return True
        
def triangle_number(n):
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
    return math.factorial(n)

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

def get_digits(n, integer=True):
    """
    get all digits from a number
    """
    if integer:
        return [int(x) for x in str(n)]
    else:
        return [str(x) for x in str(n)]

def get_int(l):
    if len(l) == 0:
        return 0
    return int("".join([str(s) for s in l]))

def is_pandigital(*args, **kwargs):
    """
    For Problem 32 & 38
    """
    num = sorted("".join(str(arg) for arg in args))
    try:
        if kwargs['length'] and len(num)!=kwargs['length']:
            return False
    except KeyError:
        pass

    for i in range(len(num)):
        if str(i+1) != str(num[i]):
            return False

    return True

def worth(word):
    return sum([int(ord(w)-ord('A')+1) for w in word.upper()])

def is_triangle_word(word):
    """
    For Problem 42
    """
    triangle_numbers = [triangle_number(i) for i in range(1, 100)]
    if worth(word) in triangle_numbers:
        return True
    else:
        return False

def pentagon_number(n):
    """
    For Problem 44
    """ 
    return n*(3*n-1)/2

def hexagon_number(n):
    """
    For Problem 45
    """
    return n*(2*n-1)

def make_primes(limit=100):
    r, i = [2], 3
    while i <= limit:
        if is_prime(i):
            r.append(i)
        i += 2
    return r

def prime_factors(n):
    """
    For Problem 47
    """
    if is_prime(n):
        return None
    g = prime_generator()
    i = 0
    r = []
    while True:
        i = g.next()
        while n % i == 0:
            n = n / i
            r.append(i)
        if n == 1:
            break
    return r

def prime_generator():
    yield 2
    n = 3 
    while True:
        if is_prime(n):
            yield n
        n += 2