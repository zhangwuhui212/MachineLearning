#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@version: 0.0.1
#@author: zhangwuhui212
#@license: default 
#@contact: zhangwuhui212@163.com
#@site: 
#@software: PyCharm
#@file: zwhUrlLoader.py
#@time: 2018/8/12 21:35

import urllib
import string

class mm_zwhUrlLoader:
    def __init__(self, _url):
        self._url = urllib.parse.quote(_url,safe=string.printable)
        #print(self._url)

    def load(self):
        headers = {
            'User-Agent': r'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          r'Chrome/45.0.2454.85 Safari/537.36 115Browser/6.0.3',
            'Referer':  self._url,
            'Connection': 'keep-alive'
        }
        data = {
            '' : ''
        }
        data = urllib.parse.urlencode(data).encode(encoding='UTF8')
        try:
            req = urllib.request.Request(self._url, headers=headers, data=data)
            page = urllib.request.urlopen(req).read().decode('utf-8')
            return page
        except urllib.error.HTTPError as e:
            print(e.code)

        return None
