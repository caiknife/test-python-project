#!/usr/bin/python
#coding: UTF-8
'''
Created on 2012-11-18
根据姓的首字母将人名排序和分组
@author: CaiKnife
'''

import itertools

def group_names(name_itertable):
    sorted_names = sorted(name_itertable, key=_sortkeyfunc)
    name_dict = {}
    for key, group in itertools.groupby(sorted_names, _groupkeyfunc):
        name_dict[key] = tuple(group)
    return name_dict

pieces_order = {2:(-1, 0), 3:(-1, 0, 1)}

def _sortkeyfunc(name):
    name_parts = name.split()
    return ''.join([name_parts[n] for n in pieces_order[len(name_parts)]])

def _groupkeyfunc(name):
    return name.split()[-1][0]