#!/usr/bin/env python
# encoding: utf-8
#@version: 0.0.1
#@author: zhangwuhui212
#@license: default 
#@contact: zhangwuhui212@163.com
#@site: 
#@software: PyCharm
#@file: download_dyzb.py
#@time: 2018/8/7 16:24 

#import module
import urllib
import re

url = "http://douyu.com"
headers = {
    'User-Agent': r'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  r'Chrome/45.0.2454.85 Safari/537.36 115Browser/6.0.3',
    'Referer': r'http://www.lagou.com/zhaopin/Python/?labelWords=label',
    'Connection': 'keep-alive'
}
req = urllib.request.Request(url, headers=headers)
page = urllib.request.urlopen(req).read()
value = page.decode('utf-8')



#打印出文件的全部内容
#print(value)

#获取相应匹配字符串,并以列表的形式进行返回
#src="https://rpic.douyucdn.cn/roomCover/2017/03/02/417441e4948021aa1de92a820abe8ece.png"
srcdata = 'src="(.*?\.(jpg|png))"'
imagelist = re.findall(srcdata,value)
#从结果来看是一个列别,其中每一个元素是一个元组[(value1),(value2).......]
#查看列表中有多少个图元素
#print(len(imagelist))

# 获取网址:print imagelist[1][0]
#i = 1
#for valueimage in imagelist:
#呵呵,临时目录一定要事先创建
#urllib.urlretrieve("https://staticlive.douyucdn.cn/upload/signs/201702171413265446.jpg", filename="C:\\download\\85.jpg")
#i += 1

#result = [("spark",100),("Hadoop",80),("Hbase",60)]

#print result[0][0]
#具体实现代码
j=0
for valueimage in imagelist:
    imageline = valueimage[0]
    print('正在下载 %s'%imageline )
    l_name= 'D:\\download\\%d.jpg'%j
    urllib.request.urlretrieve(imageline ,l_name)
    j+=1