#!/usr/bin/env python
# encoding: utf-8
#@version: 0.0.1
#@author: zhangwuhui212
#@license: default 
#@contact: zhangwuhui212@163.com
#@site: 
#@software: PyCharm
#@file: get_sina_news.py
#@time: 2018/8/6 18:51 

from bs4 import BeautifulSoup
import urllib.request,re,os

date="2018-08-06"
init_url = 'http://roll.news.sina.com.cn/interface/rollnews_ch_out_interface.php?col=89&spec=&type=&date='+date+'&ch=01&k=&offset_page=0&offset_num=0&num=60&asc=&page='

targetPath = "D:\\新浪新闻"



#定义保存文件函数
def saveFile(data,title,types,link):
    path = targetPath+"\\"+title+".txt"
    file = open(path,'wb')
    page = '题目：'+title+'\n'+'类别：'+types+'\n'+'链接：'+link+'\n'+'日期：'+date+'\n'
    file.write(page.encode('utf-8'))

    for d in data:
        file.write(d.encode('utf-8'))
    file.close()

def get_sina_content(link):
    response = urllib.request.urlopen(link)
    data = response.read()
    data = data.decode('UTF-8')
    soup=BeautifulSoup(data)

    content = ""
    for one in soup(class_="content"):
        content = str(one)
    dr = re.compile(r'<[^>]+>',re.S)
    dd = dr.sub('',content)
    print(dd)
    return dd


if __name__ == '__main__':
    page = 1
    while page:
        # 请求
        request = urllib.request.Request(init_url + str(page))
        # 爬取结果
        response = urllib.request.urlopen(request)
        data = response.read()

        # 设置解码方式
        data = data.decode('gbk')
        if data.count('channel') == 0:
            page = 0
            break
        reg_str = r'channel.*?title : "(.*?)",id.*?title : "(.*?)",url : "(.*?)",type'
        pattern = re.compile(reg_str, re.DOTALL)
        items = re.findall(pattern, data)
        #print(data)
        for item in items:
            print("类别" + item[0] + "题目：" + item[1] + "链接：" + item[2])
            #data = get_sina_content(item[2])
            #saveFile(data, item[1], item[0], item[2])
        page = 0
        #page += 1
