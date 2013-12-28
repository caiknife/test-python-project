#!/usr/bin/python
#coding: UTF-8
"""
@author: CaiKnife

compare set and list iteration speed
"""
import time
MAX = 10000000

l = list(i for i in range(MAX))
s = set(i for i in range(MAX))

start = time.time()
for n in l:
    pass
print time.time() - start

start = time.time()
for n in s:
    pass
print time.time() - start