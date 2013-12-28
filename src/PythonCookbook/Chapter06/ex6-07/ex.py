#!/usr/bin/python
#coding: UTF-8
'''
Created on 2012-11-18
有命名子项的元组
@author: CaiKnife
'''

try:
    from operator import itemgetter
except ImportError:
    def itemgetter(i):
        def getter(self):
            return self[i]
        return getter

def superTuple(typename, *attribute_names):
    nargs = len(attribute_names)
    
    class supertup(tuple):
        __slots__ = ()
        
        def __new__(cls, *args):
            if len(args) != nargs:
                raise TypeError, '%s takes exactly %d arguments (%d given)' % (typename, nargs, len(args))
            return tuple.__new__(cls, args)
        
        def __repr__(self):
            return '%s(%s)' % (typename, ', '.join(map(repr, self)))
        
    for index, attr_name in enumerate(attribute_names):
        setattr(supertup, attr_name, property(itemgetter(index)))
        
    supertup.__name__ = typename
    return supertup