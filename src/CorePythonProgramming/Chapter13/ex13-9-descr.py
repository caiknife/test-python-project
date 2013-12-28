#!/usr/bin/python
#coding:UTF-8
'''
Created on 2011-12-16

@author: ycai
'''

import os, pickle

class FileDescr(object):
    saved = []
    
    def __init__(self, name=None):
        self.name = name
        
    def __get__(self, obj, type=None):
        if self.name not in FileDescr.saved:
            raise AttributeError, '%r used before assignment' % self.name
        
        try:
            f = open(self.name, 'r')
            val = pickle.load(f)
            f.close()
            return val
        except (pickle.UnpicklingError, IOError, EOFError, AttributeError, ImportError, IndexError), e:
            raise AttributeError, 'could not read %r' % self.name
        
    def __set__(self, obj, val):
        f = open(self.name, 'w')
        
        try:
            pickle.dump(val, f)
            FileDescr.saved.append(self.name)
        except (TypeError, pickle.PicklingError), e:
            raise AttributeError, 'could not pickle %r' % self.name
        finally:
            f.close()
            
    def __delete__(self, obj):
        try:
            os.unlink(self.name)
            FileDescr.saved.remove(self.name)
        except (OSError, ValueError), e:
            pass
                        