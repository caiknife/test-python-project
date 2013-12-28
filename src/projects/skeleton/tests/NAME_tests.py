#!/usr/bin/python
#coding: UTF-8
'''
Created on 2012-12-15

@author: caiknife
'''

from nose.tools import *
import NAME

def setup():
    print "Set Up!"
    
def teardown():
    print "Tear Down!"
    
def test_basic():
    print "Just Run!"