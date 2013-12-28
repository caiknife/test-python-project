#!/usr/bin/python
#coding:UTF-8
'''
Created on 2011-12-15

@author: ycai
'''

class AnyIter(object):
    def __init__(self, data, safe=False):
        self.safe = safe
        self.iter = iter(data)
        
    def __iter__(self):
        return self
    
    def next(self, howmany=1):
        retval = []
        for eachItem in range(howmany):
            try:
                retval.append(self.iter.next())
            except StopIteration:
                if self.safe:
                    break
                else:
                    raise
        return retval
            