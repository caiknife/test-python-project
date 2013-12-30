#!/usr/bin/python
#coding: UTF-8
"""
@author: CaiKnife

Champernowne's constant
Problem 40
An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1  d10  d100  d1000  d10000  d100000  d1000000
"""


def make_irrational_fraction(length):
    n, s = 1, ""
    while len(s) < length:
        s = "".join((s, str(n)))
        n += 1
    return s


def return_int(n, length):
    if length==0:
        return 0
    return int(str(n)*length)

s = make_irrational_fraction(1000000)
d = [int(s[9*return_int(1, i)]) for i in range(7)]
print reduce(lambda x, y: x*y, d)
# print int(s[0]) * int(s[9]) * int(s[99]) * int(s[999]) * int(s[9999]) * int(s[99999]) * int(s[999999])
