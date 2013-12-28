#!/usr/bin/python
#coding: UTF-8
"""
@author: CaiKnife

http://www.pythonchallenge.com/pc/return/disproportional.html
"""

import xmlrpclib

server = xmlrpclib.Server("http://www.pythonchallenge.com/pc/phonebook.php")
print server.phone("Bert")