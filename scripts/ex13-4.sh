#!/bin/sh
#coding: UTF-8
#先查看 /tmp/test/logical 这个名称是否存在，
#若不存在则建立一个文件，使用touch建立，建立完成后离开，
#如果存在的话判断是否为文件，若为文件则将其删除后建立一个名为logical的文件，之后离开
#如果存在而且该名称为目录，则删除此目录

filepath="/tmp/test"
filename="/tmp/test/logical"

if [ ! -e "$filepath" ]; then
    mkdir "$filepath" && echo "目录${filepath}不存在，现在创建..." || exit 0
fi
cd "$filepath" && echo "进入目录${filepath}..." || exit 0

if [ ! -e "$filename" ]; then
    touch "$filename" && echo "文件${filename}不存在，现在创建..."
else
    if [ -f "$filename" ]; then
        rm -f "$filename" && touch "$filename" && echo "删除原有文件${filename}，并创建新文件..."
    fi
    if [ -d "$filename" ]; then
        rm -Rf "$filename" && echo "删除原有目录${filename}..."
    fi
fi

cd -
