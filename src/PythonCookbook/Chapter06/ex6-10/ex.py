#!/usr/bin/python
#coding: UTF-8
'''
Created on 2012-11-18
保留对被绑定方法的引用且支持垃圾回收
@author: CaiKnife
'''

import weakref, new

class ref(object):
    def __init__(self, fn):
        try:
            o, f, c = fn.im_self, fn.im_func, fn.im_class
        except AttributeError:
            self._obj = None
            self._func = fn
            self._clas = None
        else:
            if o is None:
                self._obj = None
            else:
                self._obj = weakref.ref(o)
            self._func = f
            self._clas = c
            
    def __call__(self):
        if self.obj is None:
            return self._func
        elif self._obj() is None:
            return None
        return new.instancemethod(self._func, self.obj(), self._clas)
    
