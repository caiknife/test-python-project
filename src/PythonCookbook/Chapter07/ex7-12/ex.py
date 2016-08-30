#!/usr/bin/python
# coding: UTF-8
"""
Created on 2012-11-22
在SQLite中储存BLOB
@author: CaiKnife
"""

import sqlite
import cPickle
import sqlite3


class Blob(object):
    """自动转换二进制串"""

    def __init__(self, s):
        self.s = s

    def _quote(self):
        return "'%s'" % sqlite.encode(self.s)
