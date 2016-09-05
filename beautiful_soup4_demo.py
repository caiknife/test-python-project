#!/usr/bin/env python
# coding:utf8

from bs4 import BeautifulSoup
from bs4 import __version__

print "The beautiful soup version is %s." % __version__

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

soup = BeautifulSoup(html_doc, "lxml")

print soup.title.string, type(soup.title.string)  # <class 'bs4.element.NavigableString'>
print soup.title.text, type(soup.title.text)  # <type 'unicode'>
print soup.title.string == soup.title.text  # always use .string
for a in soup.find_all(class_="sister"):
    print a.string  # directly using find_all method to get nodes

for a in soup.select('.sister'):
    print a.string  # using css selector to find nodes
