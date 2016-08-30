#!/usr/bin/python
# coding: UTF-8
"""
Created on 2012-11-4

@author: caiknife
"""
import os
import time
import sys
import sched

schedule = sched.scheduler(time.time, time.sleep)


def perform_command(cmd, inc):
    schedule.enter(inc, 0, perform_command, (cmd, inc))
    os.system(cmd)


def main(cmd, inc=60):
    schedule.enter(0, 0, perform_command, (cmd, inc))
    schedule.run()


if __name__ == '__main__':
    numargs = len(sys.argv) - 1
    if numargs < 1 or numargs > 2:
        print 'usage: ' + sys.argv[0] + ' command [seconds delay]'
        sys.exit(1)
    cmd = sys.argv[1]
    if numargs < 2:
        main(cmd)
    else:
        inc = int(sys.argv[2])
        main(cmd, inc)
