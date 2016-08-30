#!/usr/bin/python
# coding: UTF-8
"""
Created on 2013-1-16
@author: CaiKnife
"""

import os, sys

file_name = "index.txt"
content_list = [str(x) for x in range(10)]

index = file(file_name, "r")
content = [x.strip() for x in index.readlines()]
index.close()

print content_list
content_list.extend(content)
print content_list
index = file(file_name, "w")
index.writelines("\n".join(content_list))
index.close()
