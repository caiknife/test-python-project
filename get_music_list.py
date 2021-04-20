#!/usr/bin/env python
# coding:utf8

import sys, os


def main():
    try:
        filename = get_source_filename()
        print filename

        file_list = []
        if filename.endswith(".m3u"):
            final_list = process_m3u_file(filename)
        elif filename.endswith(".pls"):
            final_list = process_pls_file(filename)
        else:
            exit("No m3u or pls files provided...")

        save_to_final_list(filename, final_list)
    except Exception, e:
        print e


def process_m3u_file(filename):
    fp = file(filename)
    final_list = [line[line.find(',') + 1:] for line in fp if line.startswith("#EXTINF")]
    fp.close()
    return final_list


def process_pls_file(filename):
    fp = file(filename)
    final_list = [line[line.find('=') + 1:] for line in fp if line.startswith("Title")]
    fp.close()
    return final_list


def get_source_filename():
    args = sys.argv

    # 如果不是get_music_list.py file.m3u这种格式的话，抛出异常
    if len(args) != 2:
        raise Exception(u"Wrong number for args, please use m3u or pls files!")

    filename = str(args[1])
    if not (filename.endswith(".m3u") or filename.endswith(".pls")):
        raise Exception(u"file extension is wrong!")
    elif not os.path.exists(filename):
        raise Exception(u"file not exists!")

    return filename


def save_to_final_list(filename, final_list):
    destination_filename, extension = os.path.splitext(filename)
    destination_filename += ".txt"

    fp = file(destination_filename, "w")
    for line in final_list:
        fp.write(line)
    fp.close()


if __name__ == '__main__':
    main()
