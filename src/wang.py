#!/usr/bin/python
# coding:utf8

import os


def main():
    PATH = 'D:\\test'

    for path, dirs, files in os.walk(PATH):
        for f in files:
            if f.endswith('.py'):
                process_file(os.path.join(path, f))


def process_file(path):
    print 'writing encoding header to %s' % path
    try:
        # read content first
        fp = open(path, 'r')
        fc = fp.readlines()
        fp.close()

        if len(fc) <= 1:
            return

        # then write it back
        fp = open(path, 'w')
        # pop first line
        first_line = fc.pop(0)

        ENCODING = '# coding:utf8\n'

        if first_line == ENCODING:
            return

        if first_line == '#!/usr/bin/env python\n':
            second_line = fc.pop(0)
            if second_line == ENCODING:
                head = [first_line, ENCODING]
            else:
                head = [first_line, ENCODING, second_line]
        else:
            head = [ENCODING, first_line]
        fc = head + fc
        fp.write(''.join(fc))
        fp.close()
    except Exception, e:
        print e


if __name__ == '__main__':
    main()
    # process_file(os.path.join(os.getcwdu(), 'index_bak.py'))
