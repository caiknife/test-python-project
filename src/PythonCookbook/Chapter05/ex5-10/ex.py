#!/usr/bin/python
#coding: UTF-8
'''
Created on 2012-11-17
选取序列中最小的第n个元素
@author: CaiKnife
'''

import random
def select(data, n):
    "寻找第n个元素（最小的元素是第0个）"
    data = list(data)
    if n < 0:
        n += len(data)
    if not 0 <= n < len(data):
        raise ValueError, "can't get rank %d out of %d" % (n, len(data))
    
    while True:
        pivot = random.choice(data)
        pcount = 0
        under, over = [], []
        uappend, oappend = under.append, over.append
        for elem in data:
            if elem < pivot:
                uappend(elem)
            elif elem > pivot:
                oappend(elem)
            else:
                pcount += 1
        
        numunder = len(under)
        if n < number:
            data = under
        elif n < numunder + pcount:
            return pivot
        else:
            data = over
            n -= numunder + pcount