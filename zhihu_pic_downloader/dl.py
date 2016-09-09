#!/usr/bin/env python
# coding:utf8

import os
import sys
import requests
import re
from pyquery import PyQuery as pq

entity = {}
images = []


def main():
    try:
        get_url()
        load_page()
        save_imgs()
    except Exception, e:
        print e


def get_url():
    args = sys.argv
    # 如果不是dl.py zhihu_url这种格式的话，抛出异常
    if len(args) != 2:
        raise Exception("Wrong number for args, please use Zhihu question url!")

    zhihu_url = args[1]
    # zhihu_url不符合问题页面url格式的话，抛出异常
    re_exp = re.compile(r"^https://www\.zhihu\.com/question/(\d+)")
    match = re_exp.match(zhihu_url)
    if not match:
        raise Exception("Zhihu url is invalid!")

    entity['url'] = zhihu_url
    entity['question'] = match.groups()[0]

    print entity


def load_page():
    user_agent = "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)"
    # 构造header 伪装一下
    header = {"User-Agent": user_agent}

    resp = requests.get(entity['url'], headers=header)
    if resp.status_code != 200:
        raise Exception("Http error!")

    d = pq(resp.content)
    # imgs = d("noscript img")
    imgs = d("img.origin_image.zh-lightbox-thumb.lazy")
    for ele in imgs:
        images.append(pq(ele).attr("data-original"))


def save_imgs():
    dest_dir = os.path.dirname(os.path.abspath(__file__)) + "/images/" + entity['question']
    print dest_dir
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    for img in images:
        res = requests.get(img)
        filename = os.path.basename(img)
        fp = open(dest_dir + "/" + filename, "wb")
        fp.write(res.content)
        fp.close()
        print img + " done."


if __name__ == "__main__":
    main()
