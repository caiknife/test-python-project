#!/usr/bin/python
#coding: UTF-8
'''
Created on 2012-11-21
缓存环的实现
@author: CaiKnife
'''
from collections import deque
class RingBuffer(deque):
    """这是一个未填满的缓存类"""
    def __init__(self, size_max):
        deque.__init__(self)
        self.max = size_max
        
    def _full_append(self, x):
        deque.append(self, x)
        self.popleft()
        
    def append(self, x):
        """在缓存末尾增加一个元素"""
        deque.append(self, x)
        if len(self) == self.max:
            # 永久性地将self的类从非满变成满
            self.append = self._full_append
            
    def tolist(self):
        return list(self)
    
if __name__ == '__main__':
    x = RingBuffer(5)
    x.append(1); x.append(2); x.append(3); x.append(4)
    print x.__class__, x.tolist()
    x.append(5)
    print x.__class__, x.tolist()
    
    x.append(6)
    print x.tolist()
    x.append(7); x.append(8); x.append(9); x.append(10)
    print x.tolist()