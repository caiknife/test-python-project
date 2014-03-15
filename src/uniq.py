#!/usr/bin/python
#coding:utf8

__author__ = 'zcai'

url_list = [
    {'path': ['jy5', 'xhr', 'compose', 'init.do'], 'host': 'cwebmail.mail.163.com',
     'method': 'POST', 'query': ['cType', 'sid']},
    {'path': ['jy5', 'xhr', 'user', 'refresh.do'], 'host': 'cwebmail.mail.163.com',
     'method': 'POST', 'query': ['sid']},
    {'path': ['jy5', 'xhr', 'compose', 'compose.do'], 'host': 'cwebmail.mail.163.com',
     'method': 'POST', 'query': ['action', 'sid']},
    {'path': ['jy5', 'data', 'analytics.s'], 'host': 'cwebmail.mail.163.com', 'method': 'GET',
     'query': ['product', 'uid', 'host', 'fun', 'data', '_']},
    {'path': ['jy5', 'swf', 'upload2.swf'], 'host': 'cwebmail.mail.163.com', 'method': 'GET',
     'query': []},
    {'path': ['jy5', 'data', 'analytics.s'], 'host': 'cwebmail.mail.163.com', 'method': 'GET',
     'query': ['product', 'uid', 'host', 'fun', 'data', '_']},
    {'path': ['jy5', 'xhr', 'user', 'refresh.do'], 'host': 'cwebmail.mail.163.com',
     'method': 'POST', 'query': ['sid']},
    {'path': ['jy4-app', 'xhr', 'dropbox', 'account', 'check.do'], 'host': 'jy4-app.mail.163.com',
     'method': 'POST', 'query': ['utoken', 'sid']}
]

print url_list

print set(url_list) # error