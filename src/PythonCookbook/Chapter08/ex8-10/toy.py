#!/usr/bin/python
# coding: UTF-8
"""
Created on 2012-11-22

@author: CaiKnife
"""


def add(a, b):
    return a + b


if __name__ == '__main__':
    import doctest

    doctest.testmod()

    import unittest

    suite = doctest.DocFileSuite('test_toy.txt')
    unittest.TextTestRunner().run(suite)
