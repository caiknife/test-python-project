#!/usr/bin/python
#coding: UTF-8
"""
Created on 2012-11-23
通过SOCKET数据报传输信息
@author: CaiKnife
"""

import socket
port = 8081

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.bind(('', port))
print 'waiting on port: ', port

while True:
    data, adr = s.recvfrom(1024)
    print 'Received: ', data, ' from ', adr