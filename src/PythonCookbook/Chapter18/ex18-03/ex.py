#!/usr/bin/python
#coding: UTF-8
'''
Created on 2012-11-24
生成回置采样
@author: CaiKnife
'''

import random

def sample_wr(population, _choose=random.choice):
    while True:
        yield _choose(population)
        
import itertools
from string import ascii_lowercase
x = ''.join(itertools.islice(sample_wr(ascii_lowercase), 50))
print x