#!/usr/bin/python
# coding: UTF-8
"""
Created on 2012-11-21
Null对象设计模式的实现
@author: CaiKnife
"""


class Null(object):
    """Null对象总是很可靠的什么都不做"""

    def __new__(cls, *a, **k):
        if not hasattr(cls, '_inst'):
            cls._inst = type.__new__(cls, *a, **k)
        return cls._inst

    def __init__(self, *a, **k): pass

    def __call__(self, *a, **k): return self

    def __repr__(self): return 'Null()'

    def __nonzero__(self): return False

    def __getattr__(self, name): return self

    def __setattr__(self, name, value): return self

    def __delattr__(self, name): return self


class SeqNull(Null):
    def __len__(self): return 0

    def __iter__(self): return iter(())

    def __getitem__(self, i): return self

    def __delitem__(self, i): return self

    def __setitem__(self, i, v): return self
