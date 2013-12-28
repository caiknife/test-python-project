#!/usr/bin/python
#coding: UTF-8
'''
Created on 2013-1-10

@author: CaiKnife
'''
import os, sys, shutil, stat

def main():
    base_name = os.path.basename(__file__)
    if len(sys.argv) == 1:
        print "Format： %s %s" % (base_name, 'path_to_clear')
        sys.exit()
        
    if len(sys.argv) > 2:
        print "Error: %s can not take more than 2 params!" % (base_name)
        sys.exit()
    
    clear_svn(sys.argv[1])
    
def clear_subdir(path):
    for f in os.listdir(path):
        fp = os.path.join(path, f)
        if os.path.isfile(fp):
            os.chmod(fp, stat.S_IWRITE)
            os.remove(fp)
        else:
            clear_subdir(fp)
    
def clear_svn(path):
    if not os.path.exists(path):
        print "Error: %s does not exists!" % (path)
        sys.exit()
    
    if not os.path.isdir(path):
        print "Error: %s is not a dir!" % (path)
        sys.exit()
    
    for f in os.listdir(path):
        # 这里不可用 fp = os.path.abs(f), 必须用 fp = os.path.join(path, f)
        fp = os.path.join(path, f)
        if os.path.isdir(fp):
            if f == ".svn":
                clear_subdir(fp)
                shutil.rmtree(fp)
            else:
                clear_svn(fp)

if __name__ == '__main__':
    print "Start..."
    main()
    print "End..."
