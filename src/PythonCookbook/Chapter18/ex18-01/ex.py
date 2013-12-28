#!/usr/bin/python
#coding: UTF-8
'''
Created on 2012-11-23
消除序列中的重复
@author: CaiKnife
'''

try:
    set
except NameError:
    from sets import Set as set
    
def unique(s):
    '''返回一个无序的列表，其中没有重复'''
    try:
        return list(set(s))
    except TypeError:
        pass
    
    t = list(s)
    try:
        t.sort()
    except TypeError:
        del t
    else:
        return [x for i, x in enumerate(t) if not i or x!=t[i-1]]
    
    u = []
    for x in s:
        if x not in u:
            u.append(x)
    return u