#!/bin/bash
PATH=/bin:/sbin/:/usr/bin:/usr/sbin:/usr/local/bin/:usr/local/sbin:~/bin
export PATH

if [ "$1" == "hello" ]; then
    echo "Hello, how are you?"
elif [ -z "$1" ]; then
    echo "You MUST input parameters, ex > $0 command"
else
    echo "The ONLY parameter is 'hello'."
fi
