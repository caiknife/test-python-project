#!/usr/bin/python
# coding: UTF-8
"""
@author: CaiKnife

1000-digit Fibonacci number
Problem 25
The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn1 + Fn2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the first term in the Fibonacci sequence to contain 1000 digits?
"""

from euler import fib


def fib_generator():
    i = 1
    while True:
        yield fib(i)
        i += 1


f = fib_generator()
i = 1
while True:
    value = f.next()
    i += 1
    if len(str(value)) >= 1000:
        break

print i
