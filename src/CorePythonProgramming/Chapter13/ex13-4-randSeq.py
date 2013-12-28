#!/usr/bin/python
#coding:UTF-8
'''
Created on 2011-12-15

@author: ycai
'''

from random import choice

class RandSeq(object):
    def __init__(self, seq):
        self.data = seq
        
    def __iter__(self):
        return self
    
    def next(self):
        return choice(self.data)
    
