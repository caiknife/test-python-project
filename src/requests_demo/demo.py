#!/usr/bin/env python
# coding:utf8

import requests

r = requests.get("http://www.163.com")

print type(r.content)
print type(r.text)
