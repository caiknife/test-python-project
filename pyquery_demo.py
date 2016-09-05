#!/usr/bin/env python
# coding:utf8

from pyquery import PyQuery as pq

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

d = pq(html_doc)

for a in d('.sister'):
    element = pq(a)
    print element.attr.href, element.attr('href')
    print element.attr('class'), element.attr.class_

# d('title').insertAfter("<script></script>")

d("<script></script>").insertAfter(d("title"))
d("<link></link>").insertAfter(d("title"))

print d.html()
