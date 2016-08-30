#!/usr/bin/env python
# coding:UTF-8
"""
Created on 2011-12-6

@author: ycai
"""


def convert(func, seq):
    """conv. sequence of numbers to same type"""
    return [func(eachNum) for eachNum in seq]


myseq = (123, 45.67, -6.2e8, 999999999L)
print convert(int, myseq)
print convert(long, myseq)
print convert(float, myseq)
