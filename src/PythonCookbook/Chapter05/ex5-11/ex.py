#!/usr/bin/python
#coding: UTF-8
'''
Created on 2012-11-17
三行代码的快速排序
@author: CaiKnife
'''

def qsort(L):
    if len(L) <= 1:
        return L
    return qsort([lt for lt in L[1:] if lt < L[0]]) + L[0:1] + qsort([ge for ge in L[1:] if ge >= L[0]])

def qsort_new(x):
    if len(x)>1:
        lt = [i for i in x if cmp(i, x[0]) == -1]
        eq = [i for i in x if cmp(i, x[0]) == 0]
        gt = [i for i in x if cmp(i, x[0]) == 1]
        return qsort_new(lt) + eq + qsort_new(gt)
    else:
        return x

def qsort_test(length):
    import random
    joe = range(length)
    random.shuffle(joe)
    print joe
    qsJoe = qsort(joe)
    print qsJoe
    for i in range(len(qsJoe)):
        assert qsJoe[i] == i, 'qsort is broken at %d!' % (i)
        
if __name__ == '__main__':
    qsort_test(10)