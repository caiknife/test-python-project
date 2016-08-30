#!/bin/sh
PATH=/bin:/sbin/:/usr/bin:/usr/sbin:/usr/local/bin/:usr/local/sbin:~/bin
export PATH

echo "现在开始检测Linux系统的服务"
echo -e "将会检测www ssh ftp mail服务 \n"

testing=`netstat -tuln | grep ":80"`
if [ -n "$testing" ]; then
    echo "www服务正在运行"
fi

testing=`netstat -tuln | grep ":22"`
if [ -n "$testing" ]; then
    echo "ssh服务正在运行"
fi

testing=`netstat -tuln | grep ":21"`
if [ -n "$testing" ]; then
    echo "ftp服务正在运行"
fi

testing=`netstat -tuln | grep ":25"`
if [ -n "$testing" ]; then
    echo "mail服务正在运行"
fi
