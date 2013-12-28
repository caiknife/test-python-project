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
        raise ZipException("Usage: %s %s [%s]" % (base_name, "path_to_zip", "dest_dir"))

    if len(sys.argv) > 3:
        raise ZipException("Error: %s can not take more than 3 params." % (base_name))

    abs_path = os.path.realpath(sys.argv[1])
    if not os.path.exists(abs_path):
        raise ZipException("Error: %s does not exists!" % (abs_path))

    try:
        dest_dir = sys.argv[2]
    except IndexError:
        dest_dir = None

    make_zip(abs_path, dest_dir=dest_dir)

def make_zip(path, dest_dir=None):
    if not os.path.isdir(path):
        raise ZipException("Error: %s is not a dir!" % (path))

    zip_name = "".join([os.path.basename(path), ".zip"])
    if dest_dir:
        if not os.path.exists(dest_dir):
            os.mkdir(dest_dir, 0777)
        zip_name = os.path.join(dest_dir, zip_name)

    file_list = []
    # 追加文件夹下所有文件
    for root, dirs, files in os.walk(path):
        for name in files:
            file_list.append(os.path.join(root, name))

    zf = zipfile.ZipFile(zip_name, "w", zipfile.zlib.DEFLATED)
    for tar in file_list:
        # 获取arcname, 把同文件夹下的文件归档在一起
        arcname = tar[len(path):]
        zf.write(tar, arcname)

    zf.close()
    
if __name__ == "__main__":
    try:
        main()
    except ZipException, e:
        print e