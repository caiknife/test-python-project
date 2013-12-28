#!/bin/sh
#coding: UTF-8
#输入一个数字，计算1+2+3+...+输入的数字

read -p "请输入一个数字：" number

i=1
s=0
while [ "$i" -le "$number" ]
do
    s=$(($s+$i))
    i=$(($i+1))
done

echo "结果是: $s"
