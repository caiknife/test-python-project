#!/usr/bin/python
#coding: UTF-8
'''
Created on 2012-11-18
 避免属性读写的冗余代码
@author: CaiKnife
'''

def xproperty(fget, fset, fdel=None, doc=None):
    if isinstance(fget, str):
        attr_name = fget
        def fget(obj):
            return getattr(obj, attr_name)
    elif isinstance(fset, str):
        attr_name = fset
        def fset(obj, val):
            setattr(obj, attr_name, val)
    else:
        raise TypeError, 'either fget or fset must be a str'
    return property(fget, fset, fdel, doc)
                