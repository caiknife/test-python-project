#!/bin/bash
PATH=/bin:/sbin/:/usr/bin:/usr/sbin:/usr/local/bin/:usr/local/sbin:~/bin
export PATH

echo "The script name is: ==> $0"
[ -n "$1" ] && echo "The 1st parameter is ==> $1" || exit 0 
[ -n "$2" ] && echo "The 2nd parameter is ==> $2" || exit 0
[ -n "$3" ] && echo "The 3rd parameter is ==> $3" || exit 0
