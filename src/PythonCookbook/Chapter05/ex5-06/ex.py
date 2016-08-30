#!/usr/bin/python
# coding: UTF-8
"""
Created on 2012-11-17
以随机顺序处理列表的元素
@author: CaiKnife
"""
from random import random


def process_all_in_random_order(data, process):
    data = list(data)
    random.shuffle(data)
    for elem in data:
        process(data)


def process_random_removing(data, process):
    '''速度太慢，不考虑使用'''
    while data:
        elem = random.choice(data)
        data.remove(elem)
        process(elem)
