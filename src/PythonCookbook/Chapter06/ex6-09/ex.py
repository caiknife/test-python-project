#!/usr/bin/python
# coding: UTF-8
"""
Created on 2012-11-18

@author: CaiKnife
"""


def empty_copy(obj):
    class Empty(obj.__class__):
        def __init__(self):
            pass

    newcopy = Empty()
    newcopy.__class__ = obj.__class__
    return newcopy


class YourClass(object):
    def __init__(self):
        pass

    def __copy__(self):
        newcopy = empty_copy(self)
        return newcopy

    def __deepcopy__(self, memo):
        newcopy = empty_copy(self)
        return newcopy


if __name__ == '__main__':
    import copy

    y = YourClass()
    print y
    z = copy.copy(y)
    print z
