#!/usr/bin/python
#coding: UTF-8
'''
Created on 2012-11-23
在保留序列顺序的前提下消除其中的重复
@author: CaiKnife
'''

try:
    set
except NameError:
    from sets import Set as set
    
def uniquer(seq, f=None):
    if f is None:
        def f(x):
            return x
    
    already_seen = set()
    result = []
    for item in seq:
        marker = f(item)
        if marker not in already_seen:
            already_seen.add(marker)
            result.append(item)
    return result