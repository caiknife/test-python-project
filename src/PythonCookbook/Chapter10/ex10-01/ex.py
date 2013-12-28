#!/usr/bin/python
#coding: UTF-8
'''
Created on 2012-11-22
生成随机密码
@author: CaiKnife
'''

from random import choice
import string

def GenPasswd(length=8, chars=string.letters+string.digits):
    return ''.join([choice(chars) for i in range(length)])

if __name__ == "__main__":
    for i in range(6):
        print GenPasswd(12)