#!/usr/bin/python
# coding: UTF-8
"""
Created on 2012-11-18
检查序列的成员
@author: CaiKnife
"""


def addUnique(baseList, otherList):
    auxDict = dict.fromkeys(baseList)
    for item in otherList:
        if item not in auxDict:
            baseList.append(item)
            auxDict[item] = None
