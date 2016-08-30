#!/usr/bin/python
"""
Created on 2011-12-27

@author: CaiKnife
"""

x = ['a', 'b', 'c']
y = ['d', 'e', 'f']
z = ['g', 'h', 'i']

print map((lambda x, y, z: x + y + z), x, y, z)
print [a + b for a in x for b in y]
