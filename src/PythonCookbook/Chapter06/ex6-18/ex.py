#!/usr/bin/python
# coding: UTF-8
"""
Created on 2012-11-21
用__init__参数自动初始化实例变量
@author: CaiKnife
"""


def attributeFromDict(d):
    self = d.pop('self')
    for n, v in d.iteritems():
        setattr(self, n, v)


class Test(object):
    def __init__(self, foo, bar, baz, boom=1, bang=2):
        print locals()
        attributeFromDict(locals())


Test(1, 2, 3, 4, 5)
