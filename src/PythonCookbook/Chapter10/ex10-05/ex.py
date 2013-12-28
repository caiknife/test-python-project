#!/usr/bin/python
#coding: UTF-8
'''
Created on 2012-11-22
统计Apache的客户缓存的命中率
@author: CaiKnife
'''

def clientCachePercentage(logfile_pathname):
    contents = open(logfile_pathname, 'r')
    totalRequests = 0
    cachedRequests = 0
    
    for line in contents:
        totalRequests += 1
        if line.split(' ')[8] == '304':
            cachedRequests += 1
        
    return int(0.5+float(100*cachedRequests)/totalRequests)