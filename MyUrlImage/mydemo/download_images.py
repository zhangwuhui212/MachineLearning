#!/usr/bin/env python
# encoding: utf-8
#@version: 0.0.1
#@author: zhangwuhui212
#@license: default 
#@contact: zhangwuhui212@163.com
#@site: 
#@software: PyCharm
#@file: download_images.py
#@time: 2018/8/6 22:19

import urllib

def load_url():
    url ='http://fgj.xa.gov.cn/hd/IndexYwzxForum.aspx'
    headers = {
        'User-Agent': r'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      r'Chrome/45.0.2454.85 Safari/537.36 115Browser/6.0.3',
        'Referer': r'http://fgj.xa.gov.cn/hd/IndexYwzxForum.aspx',
        'Connection': 'keep-alive',
        'Cookie':'your cookies'
    }
    data = {
        '': '',
    }
    data = urllib.parse.urlencode(data).encode('utf-8')
    try:
        req = urllib.request.Request(url, headers=headers, data=data)
        page = urllib.request.urlopen(req).read()
        page = page.decode('utf-8')
    except urllib.error.HTTPError as e:
        print(e.code)
    print(page)

if __name__ == '__main__':
    load_url()
