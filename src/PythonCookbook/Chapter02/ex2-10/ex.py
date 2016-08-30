#!/usr/bin/python
# coding: UTF-8
"""
Created on 2012-11-3
process zip file in a string
@author: caiknife
"""

from zipfile import ZipFile

try:
    from cStringIO import StringIO
except ImportError:
    from StringIO import StringIO


class ZipString(ZipFile):
    def __init__(self, datastring):
        ZipFile.__init__(self, StringIO(datastring))
