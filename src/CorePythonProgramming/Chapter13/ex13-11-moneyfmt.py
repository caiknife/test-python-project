#!/usr/bin/python
#coding:UTF-8
'''
Created on 2011-12-19

@author: ycai
'''

class MoneyFmt(object):
    def __init__(self, value=0.0):
        self.value = value
        
    def update(self, value=None):
        pass
    
    def __repr__(self):
        return 'self.value'
    
    def __str__(self):
        val = ''
        return val
    
    def __nonzero__(self):
        return int(self.value)
    
