#!/usr/bin/python
#coding: UTF-8
'''
Created on 2012-11-18

@author: CaiKnife
'''

'''一个反应键到分数的映射的字典'''
from bisect import bisect_left, insort_left
import UserDict

class Ratings(UserDict.DictMixin, dict):
    """ Ratings类很像一个字典，但有一些额外特性：每个键
    的对应值是该键的‘分数’，所有键都根据它们的
    分数排名。对应值必须是可比较的，同样，键则必须
    是可哈希的（即可以“绑”在分数上）"""
    def __init__(self, *args, **kwds):
        '''这个类就像dict一样被实例化'''
        dict.__init__(self, *args, **kwds)
        self._rating = [(v, k) for k, v in dict.iteritems(self)]
        self._rating.sort()
        
    def copy(self):
        '''提供一个完全相同但是独立的拷贝'''
        return Ratings(self)
    
    def __setitem__(self, k, v):
        if k in self:
            del self._rating[self.rating(k)]
        dict.__setitem__(self, k, v)
        insort_left(self._rating, (v, k))
        
    def __delitem__(self, k):
        del self._rating[self.rating(k)]
        dict.__delitem__(self, k)
        
    __len__ = dict.__len__
    
    __contains__ = dict.__contains__
    
    has_key = __contains__
    
    def __iter__(self):
        for v, k in self._rating:
            yield k
            
    iterkeys = __iter__
    
    def keys(self):
        return list(self)
    
    '''三个和排名相关的方法'''
    def ratings(self, key):
        item = self[key], key
        i = bisect_left(self._rating, item)
        if item == self._rating[i]:
            return i
        raise LookupError, 'item not found in rating'
    
    def getValueByRating(self, rating):
        return self._rating[rating][0]
    
    def getKeyByRating(self, rating):
        return self._rating[rating][1]
    
def _test():
    import doctest, rating
    doctest.testmod(rating)
    
if __name__ == '__main__':
    _test()