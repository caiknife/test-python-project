#!/usr/bin/python
#coding: UTF-8
'''
Created on 2012-11-24
实现一个Bag（Multiset）收集类型
@author: CaiKnife
'''

from operator import itemgetter
from heapq import nlargest

class bag(object):
    def __init__(self, iterable=()):
        self._data = {}
        self.update(iterable)
        
    def update(self, iterable):
        if isinstance(iterable, dict):
            for elem, n in iterable.iteritems():
                self[elem] += n
        else:
            for elem in iterable:
                self[elem] += 1
    
    def __contains__(self, elem):
        return elem in self._data
    
    def __getitem__(self, elem):
        return self._data.get(elem)
    
    def __setitem__(self, elem, n):
        self._data[elem] = n
        if n == 0:
            del self._data[elem]
            
    def __delitem__(self, elem):
        self[elem] = 0
        
    def __len__(self):
        return sum(self._data.itervalues())
    
    def __nonzero__(self):
        return bool(self._data)
    
    def __eq__(self, other):
        if not isinstance(other, bag):
            return False
        return self._data == other._data
    
    def __ne__(self, other):
        return not (self == other)
    
    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, self._data)
    
    def __hash__(self):
        raise TypeError
    
    def copy(self):
        return self.__class__(self._data)
    
    __copy__ == copy
    
    def clear(self):
        self._data.clear()
        
    def __iter__(self):
        for elem, cnt in self._data.iteritems():
            for i in xrange(cnt):
                yield elem
                
    def iterunique(self):
        return self._data.iterkeys()
    
    def itercounts(self):
        return self._data.iteritems()
    
    def mostcommon(self, n=None):
        if n is None:
            return sorted(self.itercounts(), key=itemgetter(1), reverse=True)
        it = enumerate(self.itercounts())
        nl = nlargest(n, ((cnt, i, elem) for (i, (elem, cnt)) in it))
        return [(elem, cnt) for cnt, i, elem in nl]
    