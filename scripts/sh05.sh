#!/bin/bash
PATH=/bin:/sbin/:/usr/bin:/usr/sbin:/usr/local/bin/:usr/local/sbin:~/bin
export PATH

echo -e "The program will show you that filename is exist which input by you.\n"
read -p "Input a filename: " filename
test -z $filename && echo "You MUST input a filename." && exit 0

test ! -e $filename && echo "The filename $filename DO NOT exist." && exit 0

test -f $filename && filetype="regular file"
test -d $filename && filetype="directoty"
test -r $filename && perm="readable"
test -w $filename && perm="$perm writable"
test -x $filename && perm="$perm excutable"

echo "The filename: $filename is a $filetype"
echo "And the permission are: $perm"
 
