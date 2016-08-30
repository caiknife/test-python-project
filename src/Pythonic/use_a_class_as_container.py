#!/usr/bin/python
# coding: UTF-8
'''
Created on 2013-4-28
使用类作为容器
@author: CaiKnife
'''


class Container(object):
    def __init__(self, **elements):
        self.__dict__ = elements

    def __repr__(self):
        return repr(self.__dict__)

    def iteritems(self):
        for x in self.__dict__.iteritems():
            yield x


entry = Container(word="house", synonyms=['apartment', 'flat'])

print entry.word

print entry

for k, v in entry.iteritems():
    print k, "=>", v


class AnotherContainer(object):
    __slots__ = 'x', 'y'


entry = AnotherContainer()
entry.x = 1
entry.y = 2
print repr(entry)
