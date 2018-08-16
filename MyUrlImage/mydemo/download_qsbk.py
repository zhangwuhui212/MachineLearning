#!/usr/bin/env python
# encoding: utf-8
#@version: 0.0.1
#@author: zhangwuhui212
#@license: default 
#@contact: zhangwuhui212@163.com
#@site: 
#@software: PyCharm
#@file: download_qsbk.py
#@time: 2018/8/7 16:38


import urllib.request
import urllib.error
import re
import time
page = 1
url = 'http://www.qiushibaike.com/hot/page/' + str(page)
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }
count=0
try:
    request = urllib.request.Request(url, headers = headers)
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    #print(content)
    time.sleep(2)
    pattern =re.compile('<h2>(.*?)</h2>.*?<div class="content">.*?<span>(.*?)</span>.*?<div class="stats.*?class="number">(.*?)</i>', re.S)
    items = re.findall(pattern, content)

    for item in items:
        print("Author:"+item[0])
        print("Content:"+ item[1])
        print("favourite:"+ item[2])
        print("=====================")
except urllib.error.HTTPError as e:
    print(e.code)
except urllib.error.URLError as e:
    print(e.reason)
else:
    print("Executed!")