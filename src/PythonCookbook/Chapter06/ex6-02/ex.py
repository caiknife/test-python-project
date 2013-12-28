#!/usr/bin/python
#coding: UTF-8
'''
Created on 2012-11-18
定义常量
@author: CaiKnife
'''

class _const(object):
    class ConstError(TypeError):
        pass
    
    def __setattr__(self, name, value):
        if name in self.__dict__:
            raise self.ConstError, "Can't rebind const(%s)" % name
        self.__dict__[name] = value
    def __delattr__(self, name):
        if name in self.__dict__:
            raise self.ConstError, "Can't unbind const(%)" % name
        raise NameError, name
    
