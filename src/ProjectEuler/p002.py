#!/usr/bin/python
# coding: UTF-8
"""
@author: CaiKnife

Even Fibonacci numbers
Problem 2
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
"""

from euler import fib

MAX = 4000000
i = 1
results = []
while fib(i) < MAX:
    if not fib(i) % 2:
        results.append(fib(i))
    i += 1

print sum(results)
