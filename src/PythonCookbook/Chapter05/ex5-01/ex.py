#!/usr/bin/python
# coding: UTF-8
"""
Created on 2012-11-17
对字典排序
@author: CaiKnife
"""


def sortedDictValues(adict):
    keys = adict.keys()
    keys.sort()
    return [adict[key] for key in keys]
