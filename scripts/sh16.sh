#!/bin/bash
PATH=/bin:/sbin/:/usr/bin:/usr/sbin:/usr/local/bin/:usr/local/sbin:~/bin
export PATH

read -p "Please input a directory: " dir

if [ -z "$dir" ] || [ ! -d "$dir" ]; then
    echo "The $dir is NOT exist in your system"
    exit 1
fi

filelist=`ls $dir`
for filename in $filelist
do
    perm=""
    [ -r "$dir/$filename" ]  && perm="$perm readable"
    [ -w "$dir/$filename" ]  && perm="$perm writable"
    [ -x "$dir/$filename" ]  && perm="$perm executable"
    echo "The file $dir/$filename's permission is $perm."
done
