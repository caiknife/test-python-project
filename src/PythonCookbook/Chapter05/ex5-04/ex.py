#!/usr/bin/python
#coding: UTF-8
'''
Created on 2012-11-17
根据对应值将键或索引排序
@author: CaiKnife
'''

def _sorted_keys(container, keys, reverse):
    '''返回keys的列表，根据container中的对应值排序'''
    return sorted(keys, key=container.__getitem__, reverse=reverse)

class hdict(dict):
    def add(self, item, increment=1):
        '''为item的条目增加计数'''
        self[item] = increment + self.get(item, 0)
        
    def counts(self, reverse=False):
        '''根据对应值排序的键的列表'''
        return _sorted_keys(self, self, reverse)

class hlist(list):
    def __init__(self, n):
        '''初始化列表，统计n个不同项的出现'''
        list.__init__(self, n*[0])
        
    def add(self, item, increment=1):
        '''为item的条目增加计数'''
        self[item] += increment
        
    def counts(self, reverse=False):
        '''根据对应值排序的键的列表'''
        return _sorted_keys(self, xrange(len(self)), reverse)
    
sentence = '''Hello there this is a test. Hello there this was a test, but now it is not.'''
words = sentence.split()
c = hdict()
for word in words:
    c.add(word)

print 'Ascending count:'
print c.counts()
print 'Descending count:'
print c.counts(reverse=True)