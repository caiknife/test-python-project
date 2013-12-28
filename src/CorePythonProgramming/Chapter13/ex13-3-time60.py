#!/usr/bin/python
#coding:UTF-8
'''
Created on 2011-12-15

@author: ycai
'''

class Time60(object):
    'Time60 - track hours and minutes'
    
    def __init__(self, hr, min):
        'Time60 constructor - takes hours and minutes'
        self.hr = hr
        self.min = min
        
    def __str__(self):
        'Time60 - string representation'
        return '%d:%d' % (self.hr, self.min)
    
    __repr__ = __str__
    
    def __add__(self, other):
        return self.__class__(self.hr + other.hr, self.min + other.min)
    
    def __iadd__(self, other):
        self.hr += other.hr
        self.min += other.min
        return self
        