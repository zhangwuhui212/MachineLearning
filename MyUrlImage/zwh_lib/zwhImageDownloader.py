#!/usr/bin/env python
# encoding: utf-8
#@version: 0.0.1
#@author: zhangwuhui212
#@license: default 
#@contact: zhangwuhui212@163.com
#@site: 
#@software: PyCharm
#@file: zwhImageDownloader.py
#@time: 2018/8/8 13:41 

import os
import urllib
import string

class mm_zwhImageDownloader:
    def __init__(self,_img_url,_lsave_name):
        self.img_url = urllib.parse.quote(_img_url, safe=string.printable)
        self.lsave_name = _lsave_name

    def go(self):
        headers = {
            'User-Agent': r'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          r'Chrome/45.0.2454.85 Safari/537.36 115Browser/6.0.3',
            'Referer': self.img_url,
            'Connection': 'keep-alive'
        }

        data = None

        try:

            if data != None:
                data = urllib.parse.urlencode(data).encode('utf-8')

            req = urllib.request.Request(self.img_url, headers=headers, data=data)

            page = urllib.request.urlopen(req).read()
            img_file = open(self.lsave_name,'wb')
            img_file.write(page)
            img_file.close()
        except urllib.error.HTTPError as e:
            print(e.code)

    def go_r(self):
        urllib.request.urlretrieve(self.img_url, filename=self.lsave_name)

