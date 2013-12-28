#!/usr/bin/python
#coding: UTF-8
'''
Created on 2012-11-21
缓存环的实现
@author: CaiKnife
'''

class RingBuffer(object):
    """这是一个未填满的缓存类"""
    def __init__(self, size_max):
        self.max = size_max
        self.data = []
        
    class __Full(object):
        """这是一个填满了的缓存类"""
        def append(self, x):
            self.data[self.cur] = x
            self.cur = (self.cur + 1) % self.max
        
        def tolist(self):
            return self.data[self.cur:] + self.data[:self.cur]
        
    def append(self, x):
        """在缓存末尾增加一个元素"""
        self.data.append(x)
        if len(self.data) == self.max:
            self.cur = 0
            # 永久性地将self的类从非满变成满
            self.__class__ = self.__Full
            
    def tolist(self):
        return self.data
    
if __name__ == '__main__':
    x = RingBuffer(5)
    x.append(1); x.append(2); x.append(3); x.append(4)
    print x.__class__, x.tolist()
    x.append(5)
    print x.__class__, x.tolist()
    
    x.append(6)
    print x.data, x.tolist()
    x.append(7); x.append(8); x.append(9); x.append(10)
    print x.data, x.tolist()