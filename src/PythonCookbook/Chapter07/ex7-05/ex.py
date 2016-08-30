#!/usr/bin/python
# coding: UTF-8
"""
Created on 2012-11-22
Pickling被绑定方法
@author: CaiKnife
"""

import cPickle


class pickable_boundmethod(object):
    def __init__(self, mt):
        self.mt = mt

    def __getstate__(self):
        return self.mt.im_self, self.mt.im_func.__name__

    def __setstate__(self, (s, fn)):
        self.mt = getattr(s, fn)

    def __call__(self, *a, **k):
        return self.mt(*a, **k)


class Greeter(object):
    def __init__(self, name):
        self.name = name

    def greet(self):
        print 'Hello, %!' % self.name


class Repeater(object):
    def __init__(self, greeter):
        self.greeter = pickable_boundmethod(greeter)

    def greet(self):
        self.greeter()
        self.greeter()


r = Repeater(Greeter('world').greet)
s = cPickle.dumps(r)
