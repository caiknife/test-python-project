#!/usr/bin/python
#coding: UTF-8
'''
Created on 2012-11-24
生成无回置的抽样
@author: CaiKnife
'''

import random

def sample(n, r):
    "生成r个从[0, n]随机挑选并排序的整数"
    rand = random.random
    pop = n
    for samp in xrange(r, 0, -1):
        cumprob = 1.0
        x = rand()
        while x< cumprob:
            cumprob -= cumprob * samp / pop
            pop -= 1
        yield n - pop - 1