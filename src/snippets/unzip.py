#!/usr/bin/python
#coding: UTF-8
"""
Created on 2013-1-14

@author: CaiKnife
"""

import zipfile, sys, os

class ZipException(Exception):
    pass

def main():
    base_name = os.path.basename(__file__)
    if len(sys.argv) == 1:
        raise ZipException("Usage: %s %s [%s]" % (base_name, "file_to_unzip", "dest_dir"))

    if len(sys.argv) > 3:
        raise ZipException("Error: %s can not take more than 3 params." % (base_name))

    abs_path = os.path.realpath(sys.argv[1])
    if not os.path.exists(abs_path):
        raise ZipException("Error: %s does not exists!" % (abs_path))

    try:
        dest_dir = sys.argv[2]
    except IndexError:
        dest_dir = None

    extract_zip(abs_path, dest_dir=dest_dir)

def extract_zip(zip_name, dest_dir=None):
    if not os.path.isfile(zip_name):
        raise ZipException("Error: %s is not a file!" % (zip_name))

    try:
        zf = zipfile.ZipFile(zip_name)
        if not dest_dir:
            # 在当前文件夹下创建一个和压缩包同名的文件夹
            dest_dir, tail = os.path.splitext(zip_name)
        if not os.path.exists(dest_dir):
            os.mkdir(dest_dir, 0777)

        # 解压缩
        zf.extractall(dest_dir)
    except zipfile.BadZipfile:
        raise ZipException("Error: can not open %s!" % (zip_name))
  
    zf.close()


if __name__ == '__main__':
    try:
        main()
    except ZipException, e:
        print e