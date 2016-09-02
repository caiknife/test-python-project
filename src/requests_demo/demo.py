#!/usr/bin/env python
# coding:utf8
__author__ = 'caiknife'

import requests

r = requests.get("http://www.163.com")

print type(r.content)
print type(r.text)
