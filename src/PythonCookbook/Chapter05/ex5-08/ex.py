#!/usr/bin/python
# coding: UTF-8
"""
Created on 2012-11-17
获取序列中最小的几个元素
@author: CaiKnife
"""

# Python 2.3
import heapq


def isorted(data):
    data = list(data)
    heapq.heapify(data)
    while data:
        yield heapq.heappop(data)


# Python 2.4
def smallest(n, data):
    return heapq.nsmallest(n, data)
