#!/usr/bin/python
#coding: UTF-8
'''
Created on 2012-11-17
不区分大小写对字符串列表排序
@author: CaiKnife
'''

def case_insensitive_sort(string_list):
    auxiliary_list = [(x.lower(), x) for x in string_list]
    auxiliary_list.sort()
    return [x[1] for x in auxiliary_list]

def case_insensitive_sort_new(string_list):
    return sorted(string_list, key=str.lower)

