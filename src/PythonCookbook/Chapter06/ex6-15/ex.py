#!/usr/bin/python
#coding: UTF-8
'''
Created on 2012-11-21
实现单例模式
@author: CaiKnife
'''

class Singleton(object):
    '''一个Python风格的单例模式'''
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_inst'):
            cls._inst = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._inst
    
if __name__ == '__main__':
    class SingleSpam(Singleton):
        def __init__(self, s):
            self.s = s
        
        def __str__(self):
            return self.s
    
s1 = SingleSpam('spam')
print id(s1), str(s1)

s2 = SingleSpam('eggs')
print id(s1), str(s1)
print id(s2), str(s2)

assert s1 == s2
assert s1 is  s2
