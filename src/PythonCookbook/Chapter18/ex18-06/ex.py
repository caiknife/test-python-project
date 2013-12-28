#!/usr/bin/python
#coding: UTF-8
'''
Created on 2012-11-24
实现一个FIFO容器
@author: CaiKnife
'''

class Fifo(list):
    def __init__(self):
        self.back = []
        self.append = self.back.append
        
    def pop(self):
        if not self:
            self.back.reverse()
            self[:] = self.back
            del self.back[:]
        return super(Fifo, self).pop()
    
class FifoDict(dict):
    def __init__(self):
        self.nextin = 0
        self.nextout = 0
        
    def append(self, data):
        self.nextin += 1
        self[self.nextin] = data
        
    def pop(self):
        self.nextout += 1
        return dict.pop(self, self.nextout)
    
import collections
class FifoDeque(collections.deque):
    pop = collections.deque.popleft
    