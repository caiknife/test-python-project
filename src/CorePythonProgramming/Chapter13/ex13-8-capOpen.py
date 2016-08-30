#!/usr/bin/env python
# coding:UTF-8
"""
Created on 2011-12-16

@author: ycai
"""


class CapOpen(object):
    def __init__(self, fn, mode='r', buf=-1):
        self.file = open(fn, mode, buf)

    def __str__(self):
        return str(self.file)

    def __repr__(self):
        return 'self.file'

    def write(self, line):
        self.file.write(line.upper())

    def __getattr__(self, attr):
        return getattr(self.file, attr)

    def __get__(self, obj, type=None):
        pass

    def __set__(self, obj, val):
        pass


if __name__ == '__main__':
    pass
