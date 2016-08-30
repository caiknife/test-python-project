#!/usr/bin/env python
# coding: UTF-8
from itertools import groupby
from operator import methodcaller
from collections import defaultdict


def index(fname='bible/bbe.txt'):
    data = defaultdict(list)

    with open(fname) as f:
        line_number = 1
        for line in f:
            column_number = 1
            for k, g in groupby(line, key=methodcaller("isalnum")):
                if k:
                    word = ''.join(g)
                    data.setdefault(word.lower(), []).append([line_number, column_number])
                    column_number += 1
            line_number += 1
    return data


def main():
    import sys
    data = index()
    if len(sys.argv) == 1:
        for word in ['Holy', 'soul']:
            print word, data[word.lower()]
    else:
        word = sys.argv[1]
        if word in data:
            print word, data[word.lower()]
        else:
            print '...'


if __name__ == "__main__":
    main()
