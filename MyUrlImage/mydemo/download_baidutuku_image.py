#!/usr/bin/env python
# encoding: utf-8
#@version: 0.0.1
#@author: zhangwuhui212
#@license: default 
#@contact: zhangwuhui212@163.com
#@site: 
#@software: PyCharm
#@file: download_baidutuku_image.py
#@time: 2018/8/7 16:36


# 从百度图库中下载图片
import urllib
import requests
import re


def getHtml(url):
    html = requests.get(url).text
    print(html)
    urls = re.findall('"objURL":"(.*?)"', html, re.S)
    return urls

def downloadImg(urls):
    x = 1
    for url in urls:
        img = requests.get(url, allow_redirects=False)
        with open(str(x) + '.jpg', 'wb') as f:
            f.write(img.content)
            print('正在下载第%s张图片' % x)
        x += 1
        if x > 20:  # 设置爬取图片的张数
            break
    return None

if __name__ == '__main__':
    # 李沁的图片
    html = getHtml(
        'http://image.baidu.com/search/index?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8&word=李沁')
    downloadImg(html)
