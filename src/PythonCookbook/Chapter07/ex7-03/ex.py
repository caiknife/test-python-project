#!/usr/bin/python
# coding: UTF-8
"""
Created on 2012-11-22
在pickling的时候压缩
@author: CaiKnife
"""

import cPickle, gzip


def save(filename, *objects):
    f = gzip.open(filename, 'wb')
    for obj in objects:
        cPickle.dump(obj, f, 2)
    f.close()


def load(filename):
    f = gzip.open(filename, 'rb')
    while True:
        try:
            yield cPickle.load(f)
        except EOFError:
            break
    f.close()
