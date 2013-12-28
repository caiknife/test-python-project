#!/usr/bin/python
#coding:UTF-8
'''
Created on 2011-12-14

@author: ycai
'''

class RoundFloat(float):
    def __new__(self, val):
        return super(RoundFloat, self).__new__(self, round(val, 2))

class SortedKeyDict(dict):
    def keys(self):
        return sorted(super(SortedKeyDict, self).keys())

class TestMethod:
    @staticmethod
    def static_foo():
        print "Calling static method static_foo()"
        
    @classmethod
    def class_foo(cls):
        print "Calling class method class_foo()"
        print "class_foo() is part of class %s" % (cls.__name__)
        
    def normal_foo(self):
        print "Calling normal method normal_foo()"
        
if __name__ == '__main__':
    tm = TestMethod()
    
    TestMethod.static_foo()
    tm.static_foo()
    
    TestMethod.class_foo()
    tm.class_foo()
    
    t = RoundFloat(17.238)
    print t
    
    d = SortedKeyDict((('zheng-cai', 67), ('hui-jun', 68), ('xin-yi', 2)))
    print "By iterator:".ljust(12), [key for key in d]
    print "By keys():".ljust(12), d.keys()
    for k in iter(d):
        print k, d[k]
