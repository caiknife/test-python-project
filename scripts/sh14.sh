#!/bin/bash
PATH=/bin:/sbin/:/usr/bin:/usr/sbin:/usr/local/bin/:usr/local/sbin:~/bin
export PATH

s=0
for (( i=1; i<=100; i++))
do
    s=$(($s+$i))
done
echo "The result of '1+2+3+...+100' is ==> $s"
