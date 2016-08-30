#!/usr/bin/python
# coding: UTF-8
"""
Created on 2012-11-17
在增加元素时保持序列的顺序
@author: CaiKnife
"""

import heapq


class prioq(object):
    def __init__(self):
        self.q = []
        self.i = 0

    def push(self, item, cost):
        heapq.heappush(self.q, (-cost, self.i, item))
        self.i += 1

    def pop(self):
        return heapq.heappop(self.q)[-1]
