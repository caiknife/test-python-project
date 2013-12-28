#!/usr/bin/python
#coding: UTF-8
"""
@author: CaiKnife

http://www.pythonchallenge.com/pc/def/map.html
"""

def trans(char):
    asc = ord(char) + 2
    if asc > ord('z'):
        asc -= 26
    return chr(asc)

def full_trans(string):
    return ''.join([trans(x) if x.isalpha() else x for x in string])

origin_string = """
g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.
"""

new_string_list = [trans(x) if x.isalpha() else x for x in origin_string]  

print ''.join(new_string_list)
print full_trans("map")