#!/usr/bin/python
#coding: UTF-8
"""
Created on 2013-1-15
@author: CaiKnife
"""

import os, sys, re, urllib2
from pyquery import PyQuery as PQ

TARGET_SITE = "http://www.vsvod.com/"
INDEX_FILE = "index.txt"
PAGE_DIR = "pages"
PATTERN = re.compile(r"thunder://[\w/]+=*")

class VsvodException(Exception):
    pass

def main():
    # create page dir if not exists
    create_page_dir(PAGE_DIR)

    # read index file
    content_list = []
    try:
        index = file(INDEX_FILE, "r")
        content_list = [line.strip() for line in index.readlines()]
    except IOError:
        index = file(INDEX_FILE, "w")
    finally:
        index.close()

    # process main
    contents = fetch_main(TARGET_SITE)
    for name, url in contents:
        print "分析URL %s" % (url)
        if url not in content_list:
            print "%s 正在索引！" % (url)
            # process single page
            fetch_page(PAGE_DIR, name, url)
            content_list.append(url)
        else:
            print "%s 已经索引过！" % (url)

    
    # write back index file
    index = file(INDEX_FILE, "w")
    try:
        index.writelines("\n".join(content_list))
    finally:
        index.close()



def create_page_dir(dir=PAGE_DIR):
    pwd = os.getcwdu()
    page_dir = os.path.join(pwd, dir)
    if not os.path.exists(page_dir):
        os.mkdir(page_dir, 0777)

def fetch_main(url=TARGET_SITE):
    contents = []
    d = PQ(url=TARGET_SITE)
    for a in d("table:eq(3) a"):
        ele = PQ(a)
        contents.append([ele.text(), "".join((url, ele.attr('href')))])
    return contents[::-1]

def fetch_page(root_dir, name, url):
    name = name.replace(r"/", "-")
    page_dir = os.path.join(root_dir, name)
    create_page_dir(page_dir)
    
    page_file = os.path.join(page_dir, "download.txt")
    image_file = os.path.join(page_dir, "images.txt")

    # save download link
    f = urllib2.urlopen(url)
    text = f.read()
    f.close()
    match = PATTERN.findall(text)

    if match:
        download_list = []
        for m in match:
            print m
            download_list.append(m)
        df = file(page_file, "w")
        try:
            df.writelines("\n".join(download_list))
        except:
            print "Can not save download file!"
        finally:
            df.close()
    else:
        print "No match!"
    
    # get images
    images_list = []
    d = PQ(url=url)
    for img in d("table img"):
        ele = PQ(img)
        print ele.attr("src")
        images_list.append(ele.attr("src"))

    # save images
    df = file(image_file, "w")
    try:
        df.writelines("\n".join(images_list))
    except:
        print "Can not save download file!"
    finally:
        df.close()

if __name__ == '__main__':
    main()