#!/user/bin/python
# coding: UTF-8

"""
Created on 2011-11-22

@author: ycai
"""
import pprint, UserDict, os, sys

given = ['John', 'Eric', 'Terry', 'Michael']
family = ['Cleese', 'Idle', 'Gilliam', 'Palin']

pythons = UserDict.UserDict(zip(given, family))
pprint.pprint(pythons)
pprint.pprint(zip(given, family))

for root, dirs, files in os.walk(os.path.abspath(".")):
    print root
    print dirs
    print files
    sys.exit()
