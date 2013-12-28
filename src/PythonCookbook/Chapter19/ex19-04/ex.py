#!/usr/bin/python
#coding: UTF-8
'''
Created on 2012-11-25
在多重赋值中拆解部分项
@author: CaiKnife
'''

def peel(iterable, arg_cnt=1):
    '''获得一个可迭代对象的前arg_cnt项，然后用一个迭代器表示余下的部分'''
    iterator = iter(iterable)
    
    for num in xrange(arg_cnt):
        yield iterator.next()
    yield iterator
    
if __name__ == '__main__':
    t5 = range(1, 6)
    a, b, c= peel(t5, 2)
    print a, b, list(c)