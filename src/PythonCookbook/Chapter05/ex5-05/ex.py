#!/usr/bin/python
#coding: UTF-8
'''
Created on 2012-11-17

@author: CaiKnife
'''

import re
re_digits = re.compile(r'(\d+)')

def embedded_numbers(s):
    pieces = re_digits.split(s)
    pieces[1::2] = map(int, pieces[1::2])
    return pieces

def sort_strings_with_embedded_numbers(alist):
    return sorted(alist, key=embedded_numbers)

files = 'file3.txt file11.txt file7.txt file4.txt file15.txt'.strip().split()
print ' '.join(sort_strings_with_embedded_numbers(files))