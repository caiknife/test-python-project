#!/usr/bin/python
#coding: UTF-8
'''
Created on 2012-11-23
过滤FTP站点列表
@author: CaiKnife
'''

import socket, ftplib

def isFTPSiteUp(site):
    try:
        ftplib.FTP(site).quit()
    except socket.error:
        return False
    else:
        return True
    
def filterFTPsites(sites):
    return [site for site in sites if isFTPSiteUp(site)]

