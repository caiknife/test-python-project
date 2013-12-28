#!/usr/bin/python
#coding: UTF-8
'''
Created on 2012-11-3
load data from zip file
@author: caiknife
'''

import zipfile, tempfile, os, sys
handle, filename = tempfile.mkstemp('.zip')
os.close(handle)

z = zipfile.ZipFile(filename, 'w')
z.writestr('hello.py', 'def f(): return "Hello world from " + __file__\n')
z.close()
sys.path.insert(0, filename)

import hello
print hello.f()

os.unlink(filename)