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

#使用我自己的ID登录成功，验证 打印出来的html不包含验证码字段
#验证码地址动态改变
#http://fgj.xa.gov.cn/hd/rndimage.aspx

import urllib

import http.cookiejar

from bs4 import BeautifulSoup

def login():
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
        #page = page.decode('utf-8')
    except urllib.error.HTTPError as e:
        print(e.code)
    #print(page)
    h = open('D:\\ffjgw.html','wb')
    h.write(page)
    h.close()


def login_1():
    url = 'http://fgj.xa.gov.cn/hd/IndexYwzxForum.aspx'
    headers = {
        'User-Agent': r'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      r'Chrome/45.0.2454.85 Safari/537.36 115Browser/6.0.3',
        'Referer': r'http://fgj.xa.gov.cn/hd/IndexYwzxForum.aspx',
        'Connection': 'keep-alive'
    }
    data = {
        # '__VIEWSTATE': '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',
        # '__VIEWSTATEGENERATOR': '6B059315',
        # '__EVENTVALIDATION':'/wEWGwKE+6ugAgLLgpzlCwK9pJS0CAKdivS2CgLRyK7kBQK256LXAQLfi4frDwLR0MDsCwLeucmEDwKT+7uQCALsud6BBgLxuP3fBgLB+pWoAwLkz+GNCQLy9pSkCQLCorq9AwKigeq+AgK1kKjqDALY8fu/BQLHtI3OBALl1bxmAuDX398PAqWpiswDAqakz6UMAq7bmrwIAsrCq4IJAuiXhc0DrXLY3W1eEat+eQcxkW6tDqDEA6iXoeUPcos0pNJCYac=',
        'WUCMemberLogin1_txt_userName': 'your username',
        'WUCMemberLogin1_txt_password': 'you password',
        'WUCMemberLogin1_txtCheckCode': 'yanzhengma',
        'WUCMemberLogin1_btn_login': '登 录'
    }
    data = urllib.parse.urlencode(data).encode('utf-8')
    try:
        req = urllib.request.Request(url, headers=headers, data=data)
        page = urllib.request.urlopen(req).read()
        # page = page.decode('utf-8')
    except urllib.error.HTTPError as e:
        print(e.code)
    # print(page)
    h = open('D:\\ffjgw.html', 'wb')
    h.write(page)
    h.close()

def extract_image(ht_img):
    from PIL import Image
    from io import BytesIO

    img_data = ht_img.get('src')
    print(img_data)
    img_data = img_data.partition(',')[-1]
    #print(img_data)
    # binary_img_data = img_data.decode('base64')
    #
    # file_like = BytesIO(binary_img_data)
    # img = Image.open(file_like)
    # img.save('D:\\test.png')


def prase_html(html):
    soup = BeautifulSoup(html, 'html.parser')

    if 0:
        img2 = soup.select('div #WUCMemberLogin_div_login td #imgCode')
        print(img2)

    if 1:
        results = {}
        results['imgCode'] = soup.find('body').find('div', id = 'WUCMemberLogin_div_login').find('table').find('img', id = 'imgCode')
        extract_image(results['imgCode'])
        #print(results)

def login_3():
    url = 'http://fgj.xa.gov.cn/hd/IndexYwzxForum.aspx'
    headers = {
        'User-Agent': r'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      r'Chrome/45.0.2454.85 Safari/537.36 115Browser/6.0.3',
        'Referer': r'http://www.lagou.com/zhaopin/Python/?labelWords=label',
        'Connection': 'keep-alive'
    }
    req = urllib.request.Request(url, headers=headers)
    page = urllib.request.urlopen(req).read()
    page = page.decode('utf-8')
    prase_html(page)
    #print(page)

def login_4():
    try:
        url_login = "https://www.zhihu.com/#signin"
        url_captcha = 'http://www.zhihu.com/captcha.gif?r=%d&type=login&lang=cn' % (time.time() * 1000)
        login_content = self.request_session.get(url_login).content
        soup = BeautifulSoup(login_content, 'lxml')
        # find 方法第二个参数还可以是 python 编译的正则表达式
        # 譬如soup.find_all("a", href=re.compile(r"/item/\w+"))
        xsrf = soup.find('input', attrs={'name': '_xsrf'})['value']
        captcha_content = self.request_session.get(url_captcha).content
        return {'xsrf': xsrf, 'captcha_content': captcha_content}
    except Exception as e:
        print('get login xsrf and captcha failed!' + str(e))
        return dict()

import chardet

def get_web_bm():
    response = urllib.request.urlopen("http://fanyi.baidu.com/")
    html = response.read()
    charset = chardet.detect(html)
    print(charset)

def save_web_info():
    #urlretrieve方法将url定位到的html文件下载到你本地的硬盘中
    tuple = urllib.request.urlretrieve("http://f12.baidu.com/it/u=800947190,1491613681&fm=72", filename="D:\\1.png")
    print(tuple)

if __name__ == '__main__':
    #login_4()
    save_web_info()
