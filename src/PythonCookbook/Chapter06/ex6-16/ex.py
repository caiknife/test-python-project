#!/usr/bin/python
#coding: UTF-8
'''
Created on 2012-11-21
用Borg惯用法来避免“单例”模式
@author: CaiKnife
'''

class Borg(object):
    _shared_state = {}
    
    def __new__(cls, *a, **k):
        obj = object.__new__(cls, *a, **k)
        obj.__dict__ = cls._shared_state
        return obj
    
if __name__ == '__main__':
    class Example(Borg):
        name = None
        
        def __init__(self, name=None):
            if name is not None:
                self.name = name
        
        def __str__(self):
            return 'name->%s' % self.name
        
a = Example('Lara')
b = Example()
print a, b

c = Example('John Malkovich')
print a, b, c

b.name = 'John'
print a, b, c
