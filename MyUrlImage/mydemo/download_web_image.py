#!/usr/bin/env python
# encoding: utf-8
#@version: 0.0.1
#@author: zhangwuhui212
#@license: default 
#@contact: zhangwuhui212@163.com
#@site: 
#@software: PyCharm
#@file: download_web_image.py
#@time: 2018/8/6 23:50 

from bs4 import BeautifulSoup
import requests,os
targetDir = os.path.join(os.path.dirname(os.path.abspath(__file__)),'imgs1')#图片保存的路径，eg,向前文件夹为'D:\Coding', 即图片保存在'D:\Coding\imgs1\'
if not os.path.isdir(targetDir):#不存在创建路径
    os.mkdir(targetDir)
url = 'http://fgj.xa.gov.cn/hd/IndexYwzxForum.aspx'
domain = 'http://fgj.xa.gov.cn/hd/'
#保存页面到本地
def save_html():
    r_page = requests.get(url)
    f = open('page.html','wb')
    f.write(r_page.content)#save to page.html
    f.close()
    return r_page
#修改文件,将图片路径改为本地的路径
def update_file(old,new):
    with open('page.html', encoding='utf-8') as f, open('page_bak.html', 'w',
                                                   encoding='utf-8') as fw:  # 打开两个文件，原始文件用来读，另一个文件将修改的内容写入
        for line in f:  # 遍历每行，取出来的是字符串，因此可以用replace 方法替换
            new_line = line.replace(old, new)  # 逐行替换
            fw.write(new_line)  # 写入新文件
    os.remove('page.html')  # 删除原始文件
    os.rename('page_bak.html', 'page.html')  # 修改新文件名， old -> new
#保存图片到本地
def save_file_to_local():
    obj = BeautifulSoup(save_html().content, 'html.parser')  # 后面是指定使用lxml解析，lxml解析速度比较快，容错高。
    imgs = obj.find_all('body')
    #将页面上图片的链接加入list
    urls = []
    for img in imgs:
        print(img)
        if 'data-src' in str(img):
            urls.append(img['data-src'])
        else:
            urls.append(img['src'])
    #遍历所有图片链接，将图片保存到本地指定文件夹，图片名字用0，1，2...
    # i = 0
    # for url in urls:#看下文章的图片有哪些格式，一一处理
    #     if url.startswith('//'):
    #         new_url = 'http:' + url
    #         r = requests.get(new_url)
    #     elif url.startswith('/') and url.endswith('gif'):
    #         new_url = domain + url
    #         r = requests.get(new_url)
    #     elif url.endswith('.png') or url.endswith('jpg') or url.endswith('gif'):
    #         r = requests.get(url)
    #     t = os.path.join(targetDir, str(i) + '.jpg')#指定目录
    #     print('save path:', t)
    #     fw = open(t,'wb')  # 指定绝对路径
    #     fw.write(r.content)#保存图片到本地指定目录
    #     i += 1
    #     update_file(url,t)#将老的链接(有可能是相对链接)修改为本地的链接，这样本地打开整个html就能访问图片
    #     fw.close()

if __name__ == '__main__':
    save_html()
    save_file_to_local()