#!/usr/bin/python
#coding: UTF-8
'''
Created on 2012-11-25
生成Fibonacci数列
@author: CaiKnife
'''

def fib():
    '''Fibonacci数列的无界生成器'''
    x, y = 0, 1
    while True:
        yield x
        x, y = y, x + y
        
if __name__ == '__main__':
    import itertools
    print list(itertools.islice(fib(), 10))