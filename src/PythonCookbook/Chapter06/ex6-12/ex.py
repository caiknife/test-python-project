#!/usr/bin/python
# coding: UTF-8
"""
Created on 2012-11-21
检查一个实例的状态变化
@author: CaiKnife
"""
import copy


class ChangeCheckerMinin(object):
    containerItems = {dict: dict.iteritems, list: enumerate}
    immutable = False

    def snapshot(self):
        if self.immutable:
            return
        self._snapshot = self._copy_container(self.__dict__)

    def makeImmutable(self):
        self.immutable = True
        try:
            del self._snapshot
        except AttributeError:
            pass

    def _copy_container(self, container):
        """半浅拷贝，只对容器类型递归"""
        new_container = copy.copy(container)
        for k, v in self.containerItems[type(new_container)](new_container):
            if type(v) in self.containerItems:
                new_container[k] = self._copy_container(v)
            elif hasattr(v, 'snapshot'):
                v.snapshot()
        return new_container

    def isChanged(self):
        if self.immutable:
            return False
        snap = self.__dict__.pop('_snapshot', None)
        if snap is None:
            return True
        try:
            return self._checkContainer(self.__dict__, snap)
        finally:
            self._snapshot = snap

    def _checkContainer(self, container, snapshot):
        if len(container) != len(snapshot):
            return True
        for k, v in self.containerItems[type(container)](container):
            try:
                ov = snapshot[k]
            except LookupError:
                return True
            if self._checkItem(v, ov):
                return True
        return False

    def _checkItem(self, newitem, olditem):
        if type(newitem) != type(olditem):
            return True
        if type(newitem) in self.containerItems:
            return self._checkContainer(newitem, olditem)
        if newitem is olditem:
            method_isChanged = getattr(newitem, 'isChanged', None)
            if method_isChanged is None:
                return False
            return method_isChanged()
        return newitem != olditem


if __name__ == '__main__':
    class eg(ChangeCheckerMinin):
        def __init__(self, *a, **k):
            self.L = list(*a, **k)

        def __str__(self):
            return "eg(%s)" % str(self.L)

        def __getattr__(self, a):
            return getattr(self.L, a)


    x = eg('ciao')
    print 'x=', x, 'is changed =', x.isChanged()
    x.snapshot()
    print 'x=', x, 'is changed =', x.isChanged()
    x.append('x')
    print 'x=', x, 'is changed =', x.isChanged()
    print x.__dict__
