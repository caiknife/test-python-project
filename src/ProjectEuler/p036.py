#!/usr/bin/python
# coding: UTF-8
"""
@author: CaiKnife

Double-base palindromes
Problem 36
The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)

"""


def to_binary(n):
    return int(str(bin(n))[2:])


def is_palindrome(n):
    r = int(str(n)[::-1])
    return r == n


print sum([i for i in range(1000001) if is_palindrome(i) and is_palindrome(to_binary(i))])
