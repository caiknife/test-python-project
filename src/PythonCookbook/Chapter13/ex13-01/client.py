#!/usr/bin/python
# coding: UTF-8
"""
Created on 2012-11-23

@author: CaiKnife
"""

import socket

port = 8081

host = 'localhost'
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.sendto("Holy Guido! It's working.", (host, port))
