#!/usr/bin/python
# coding: UTF-8
"""
Created on 2012-11-24
编写一个类似range的浮点数递增的函数
@author: CaiKnife
"""""

import itertools


def frange(start, end=None, inc=1.0):
    """一个类似xrange的生成器，生成浮点数"""
    if end is None:
        end = start + 0.0
        start = 0.0

    assert inc

    for i in itertools.count():
        next = start + i * inc
        if (inc > 0.0 and next >= end) or (inc < 0.0 and next <= end):
            break
        yield next
