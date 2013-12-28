#!/bin/bash
PATH=/bin:/sbin/:/usr/bin:/usr/sbin:/usr/local/bin/:usr/local/sbin:~/bin
export PATH

echo "This program will try to calculate:"
echo "How many days about your demobilization date..."
read -p "Please input your demobilization date (YYYYMMDD ex>20050401)" date2

date_d=`echo $date2 | grep '[0-9]\{8\}'`

if [ -z "$date_d" ]; then
    echo "your input the wrong format of date..."
    exit 0
fi

declare -i date_dem=`date --date="$date2" +%s`
declare -i date_now=`date +%s`
declare -i date_total_s=$(($date_dem-$date_now))
declare -i date_d=$(($date_total_s/60/60/24))

if [ "$date_total_s" -lt "0" ]; then
    echo "You had been demobilization before " $((-1*$date_d)) " ago."
else
    declare -i date_h=$(($(($date_total_s-$date_d*60*60*24))/60/60))
    echo "You will be demobilized after $date_d days and $date_h hours."
fi
