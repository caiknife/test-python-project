#!/usr/bin/python
# coding: UTF-8
"""
Created on 2012-11-18

@author: CaiKnife
"""


class Proxy(object):
    """所有代理的基类"""

    def __init__(self, obj):
        super(Proxy, self).__init__(obj)
        self._obj = obj

    def __getattr__(self, attrib):
        return getattr(self._obj, attrib)


def make_binder(unbound_method):
    def f(self, *a, **k):
        return unbound_method(self._obj, *a, **k)

    f.__name__ = unbound_method.__name__
    return f


known_proxy_classes = {}


def proxy(obj, *specials):
    """能够委托特殊方法的代理的工厂方法"""
    obj_cls = obj.__class__
    key = obj_cls, specials
    cls = known_proxy_classes.get(key)
    if cls is None:
        cls = type("%sProxy" % obj_cls.__name__, (Proxy,), {})
        for name in specials:
            name = '__%s__' % name
            unbound_method = getattr(obj_cls, name)
            setattr(cls, name, make_binder(unbound_method))
        known_proxy_classes[key] = cls
    return cls(obj)
