#!/usr/bin/python
# coding: UTF-8
"""
Created on 2012-11-18
链式字典查询
@author: CaiKnife
"""


class ChainMap(object):
    def __init__(self, *mappings):
        self._mappings = mappings

    def __getitem__(self, key):
        for mapping in self._mappings:
            try:
                return mapping[key]
            except KeyError:
                pass

        raise KeyError, key

    def get(self, key, default=None):
        try:
            return self._mappings[key]
        except KeyError:
            return default

    def __contains__(self, key):
        try:
            self[key]
            return True
        except KeyError:
            return False


import UserDict
from sets import Set


class FullChainMap(ChainMap, UserDict.DictMixin):
    def copy(self):
        return self.__class__(self._mappings)

    def __iter__(self):
        seen = Set()
        for mapping in self._mappings:
            for key in mapping:
                if key not in seen:
                    yield key
                    seen.add(key)

    iterkeys = __iter__

    def keys(self):
        return list(self)
