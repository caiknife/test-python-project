#!/usr/bin/python
#coding: UTF-8
'''
Created on 2012-11-23
从Web抓取文档
@author: CaiKnife
'''

from urllib import urlopen

doc = urlopen('http://www.python.org').read()
print doc
doc = urlopen('http://www.python.org')
print doc.info()