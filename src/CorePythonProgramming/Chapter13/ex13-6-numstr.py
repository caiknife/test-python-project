#!/usr/bin/python
#coding:UTF-8
'''
Created on 2011-12-15

@author: ycai
'''

class NumStr(object):
    def __init__(self, num=0, string=''):
        self.__num = num
        self.__string = string
        
    def __str__(self):
        return '[%d::%s]' % (self.__num, self.__string)
    
    __repr__ = __str__
    
    def __add__(self, other):
        if isinstance(other, NumStr):
            return self.__class__(self.__num + other.__num, self.__string + other.__string)
        else:
            raise TypeError, 'Illegal argument type for built-in operation'
        
    def __mul__(self, num):
        if isinstance(num, int):
            return self.__class__(self.__num * num, self.__string * num)
        else:
            raise TypeError, 'Illegal argument type for built-in operation'
        
    def __nonzero__(self):
        return self.__num or len(self.__string)
    
    def __normal_cval(self, cmpres):
        return cmp(cmpres, 0)
    
    def __cmp__(self, other):
        assert isinstance(other, NumStr), 'Illegal argument type for built-in operation'
        return self.__normal_cval(cmp(self.__num, other.__num)) + self.__normal_cval(cmp(self.__string, other.__string))
    
if __name__ == '__main__':
    a = NumStr(3, 'foo')
    b = NumStr(3, 'goo')
    c = NumStr(2, 'foo')
    d = NumStr()
    e = NumStr(string='boo')
    f = NumStr(1)
    
    print a
    print b
    print c
    print d
    print e
    print f
    print a < b
    print b < c
    print a == a
    print b * 2
    print b + e
    print e + b
    if d:
        print 'd is not false'
    if e:
        print 'e is not false'
    print cmp(a, b)
    print cmp(a, c)
    print cmp(a, a) 
    