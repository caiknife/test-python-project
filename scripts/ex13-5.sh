#!/bin/bash
#coding: UTF-8
#取出/etc/passwd的第一栏，每一栏以字符串“the 1 account is 'root'”来显示，1表示行数

cat "/etc/passwd" | awk 'BEGIN {FS=":"} {print "第" NR "个账户是：" $1}'
