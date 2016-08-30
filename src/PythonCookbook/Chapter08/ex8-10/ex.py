#!/usr/bin/python
# coding: UTF-8
"""
Created on 2012-11-22
在Python2.4中使用doctest和unittest
@author: CaiKnife
"""


def add(a, b):
    """将任意两个对象相加并返回和"""
    return a + b


if __name__ == '__main__':
    import doctest

    doctest.testmod()

    import unittest

    suite = doctest.DocFileSuite('test_toy.txt')
    unittest.TextTestRunner().run(suite)
