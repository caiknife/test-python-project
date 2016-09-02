#!/usr/bin/env python
# coding:utf8

import requests

r = requests.get("http://www.163.com")

print type(r.content)
print type(r.text)

r = requests.post('http://httpbin.org/post', data={'key': 'value'})

print r.url
print r.encoding
