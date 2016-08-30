#!/bin/bash
#coding: UTF-8
#这个脚本用来计算还有多少天过生日

birth_md="0815"
this_year=`date +%Y`
next_year=`date --date="+1 year" +%Y`
this_birthday="$this_year""$birth_md"
next_birthday="$next_year""$birth_md"
today=`date +%Y%m%d`
today_s=`date +%s`

if [ "$today" -gt "$this_birthday" ]; then
    dest_s=`date --date="$next_birthday" +%s`
else
    dest_s=`date --date="$this_birthday" +%s`
    next_birthday="$this_birthday"
fi

s_d=$(($(($dest_s-$today_s))/60/60/24))

echo -e "你的下一个生日是："`date --date="$next_birthday" +%Y年%m月%d日`"，距离那一天还有 $s_d 天。"
