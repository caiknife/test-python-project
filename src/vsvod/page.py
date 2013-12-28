#!/usr/bin/python
#coding: UTF-8
"""
@author: CaiKnife
"""

import os, sys, urllib2, re

class PageException(Exception):
    pass

def main():
    if len(sys.argv) == 1:
        raise PageException("Usage: page.py url")
    elif len(sys.argv) > 2:
        raise PageException("Error: Can not take more than 2 params!")

    url = sys.argv[1]
    source = load_page(url=url)
    get_image_urls(source=source)

def load_page(url=None):
    if not url:
        raise PageException("Error: No url offered!")

    source = ""
    try:
        f = urllib2.urlopen(url)
        #print f.info()
        source = f.read()
    except (urllib2.HTTPError, ValueError), e:
        raise PageException(e)
    finally:
        try:
            f.close()
        except UnboundLocalError, e:
            pass

    return source

def get_image_urls(source=None):
    if not source:
        raise PageException("Error: Source is empty!")

    pattern = re.compile(r'src="(?P<src>http://(?P<domain>[\w\.]+)/[\w/]+\.jpg)"', re.IGNORECASE)
    match = pattern.finditer(source)
    if match:
        for m in match:
            print m.groupdict()['src']
    else:
        raise PageException("Error: No match found!")


if __name__ == '__main__':
    try:
        main()
    except PageException, e:
        print e