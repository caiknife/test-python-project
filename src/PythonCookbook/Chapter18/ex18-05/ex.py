#!/usr/bin/python
# coding: UTF-8
"""
Created on 2012-11-24
缓存函数的返回值
@author: CaiKnife
"""


def memoize(fn):
    memo = {}

    def memoizer(*a, **k):
        if k:
            memoizer.namedargs += 1
            return fn(*a, **k)
        try:
            memoizer.cacheable += 1
            try:
                return memo[a]
            except KeyError:
                memoizer.misses += 1
                memo[a] = result = fn(*a)
                return result
        except TypeError:
            memoizer.cacheable -= 1
            memoizer.noncacheable += 1
            return fn(*a)

    memoizer.namedargs = memoizer.cacheable = memoizer.noncacheable = 0
    memoizer.misses = 0
    return memoizer


@memoize
def fib(n):
    if n < 2:
        return 1
    return fib(n - 1) + fib(n - 2)
