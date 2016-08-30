#!/usr/bin/python
# coding: UTF-8
"""
Created on 2012-11-22
统计Apache中每个IP的点击率
@author: CaiKnife
"""


def calculateApacheIpHits(logfile_pathname):
    ipHitListing = {}
    contents = open(logfile_pathname, 'r')

    import re
    ip_specs = r'\.'.join([r'\d{1,3}' * 4])
    re_ip = re.compile(ip_specs)
    for line in contents:
        match = re_ip.match(line)
        if match:
            ip = match.group()
            ipHitListing[ip] = ipHitListing.get(ip, 0) + 1
    return ipHitListing
