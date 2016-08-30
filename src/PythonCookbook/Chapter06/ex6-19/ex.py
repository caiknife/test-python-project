#!/usr/bin/python
# coding: UTF-8
"""
Created on 2012-11-21
调用超类的__init__方法
@author: CaiKnife
"""


class ClassicClass():
    pass


class NewStyleClass(object):
    pass


x1 = ClassicClass()
x2 = NewStyleClass()

print x1.__class__, type(x1)
print x2.__class__, type(x2)
