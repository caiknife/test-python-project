#!/usr/bin/python
# coding: UTF-8
"""
@author: CaiKnife
"""
bound = xrange(1, 10)
result = [(x, y, z) for x in bound for y in bound for z in bound if (x * 10 + y) * x == 111 * z]
print result
