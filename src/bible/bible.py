#!/usr/lib/python
from bible_lib import process_line
import os, time

if __name__ == '__main__':
    cur_dir = os.getcwd()
    handle = file(os.path.join(cur_dir, 'bbe.txt'), 'r')
    start = time.time()
    try:
        l = 1
        for line in handle:
            process_line(l, line)
            l += 1
    finally:
        handle.close()
    end = time.time()
    print end - start
