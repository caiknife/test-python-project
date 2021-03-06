#!/usr/bin/python
# coding: UTF-8
"""
Created on 2012-11-18
温标的转换
@author: CaiKnife
"""


class Temperature(object):
    coefficients = {
        'c': (1.0, 0.0, -273.15),
        'f': (1.8, -273.15, 32.0),
        'r': (1.8, 0.0, 0.0)
    }

    def __init__(self, **kwds):
        try:
            name, value = kwds.popitem()
        except KeyError:
            name, value = 'k', 0

        if kwds or name not in 'kfcr':
            kwds[name] = value
            raise TypeError, 'invalid arguments %r' % (kwds)
        setattr(self, name, float(value))

    def __getattr__(self, name):
        try:
            eq = self.coefficients[name]
        except KeyError:
            raise AttributeError, name
        return (self.k + eq[1]) * eq[0] + eq[2]

    def __setattr__(self, name, value):
        if name in self.coefficients:
            eq = self.coefficients[name]
            self.k = (value - eq[2]) / eq[0] - eq[1]
        elif name == 'k':
            object.__setattr__(self, name, value)
        else:
            raise AttributeError, name

    def __str__(self):
        return '%s K' % self.k

    def __repr__(self):
        return 'Temperature(k=%r)' % self.k
