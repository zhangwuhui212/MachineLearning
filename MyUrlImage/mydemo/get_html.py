#!/usr/bin/env python
# encoding: utf-8
#@version: 0.0.1
#@author: zhangwuhui212
#@license: default 
#@contact: zhangwuhui212@163.com
#@site: 
#@software: PyCharm
#@file: get_html.py
#@time: 2018/8/6 18:01

from urllib import request

from bs4 import BeautifulSoup
import urllib.request


def get_url_1():
    response = request.urlopen(r'http://python.org/')
    page = response.read()
    page = page.decode('utf-8')
    print(page)

def get_url_2():
    #使用Request
    url = r'http://www.lagou.com/zhaopin/Python/?labelWords=label'
    headers = {
        'User-Agent': r'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      r'Chrome/45.0.2454.85 Safari/537.36 115Browser/6.0.3',
        'Referer': r'http://www.lagou.com/zhaopin/Python/?labelWords=label',
        'Connection': 'keep-alive'
    }
    req = request.Request(url, headers=headers)
    page = request.urlopen(req).read()
    page = page.decode('utf-8')
    print(page)

def get_url_3():
    #Post数据
    #urlopen（）的data参数默认为None，当data参数不为空的时候，urlopen（）提交方式为Post。
    from urllib import request, parse
    url = r'http://www.lagou.com/jobs/positionAjax.json?'
    headers = {
        'User-Agent': r'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      r'Chrome/45.0.2454.85 Safari/537.36 115Browser/6.0.3',
        'Referer': r'http://www.lagou.com/zhaopin/Python/?labelWords=label',
        'Connection': 'keep-alive'
    }
    data = {
        'first': 'true',
        'pn': 1,
        'kd': 'Python'
    }
    data = parse.urlencode(data).encode('utf-8')
    try:
        req = request.Request(url, headers=headers, data=data)
        page = request.urlopen(req).read()
        page = page.decode('utf-8')
    except urllib.error.HTTPError as e:
        print(e.code)
    print(page)

def get_url_4():
    #Post数据
    #urlopen（）的data参数默认为None，当data参数不为空的时候，urlopen（）提交方式为Post。
    from urllib import request, parse
    url = r'http://www.lagou.com/jobs/positionAjax.json?'
    headers = {
        'User-Agent': r'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      r'Chrome/45.0.2454.85 Safari/537.36 115Browser/6.0.3',
        'Referer': r'http://www.lagou.com/zhaopin/Python/?labelWords=label',
        'Connection': 'keep-alive'
    }
    data = {
        'first': 'true',
        'pn': 1,
        'kd': 'Python'
    }
    proxy = request.ProxyHandler({'http': '27.17.32.142:80'})  # 设置proxy
    opener = request.build_opener(proxy)  # 挂载opener
    request.install_opener(opener)  # 安装opener
    data = parse.urlencode(data).encode('utf-8')
    page = opener.open(url, data).read()
    page = page.decode('utf-8')
    print(page)

def get_url_5():
    #使用代理
    proxy_support = urllib.request.ProxyHandler({'sock5': 'localhost:1080'})
    opener = urllib.request.build_opener(proxy_support)
    urllib.request.install_opener(opener)
    a = urllib.request.urlopen("http://www.python.org/").read().decode("utf8")
    print(a)

def get_url_6():
    #HTTP 认证
    # create a password manager
    password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
    # Add the username and password.
    # If we knew the realm, we could use it instead of None.
    top_level_url = "http://www.renren.com/"
    password_mgr.add_password(None, top_level_url, 'zhangwuhui212@163.com', 'lwn463523')
    handler = urllib.request.HTTPBasicAuthHandler(password_mgr)
    # create "opener" (OpenerDirector instance)
    opener = urllib.request.build_opener(handler)
    # use the opener to fetch a URL
    a_url = "http://sc.renren.com/scores/mycalendar"
    x = opener.open(a_url)
    print(x.read())
    # Install the opener.
    # Now all calls to urllib.request.urlopen use our opener.
    urllib.request.install_opener(opener)
    a = urllib.request.urlopen(a_url).read().decode('utf8')
    print(a)

def prase_html(html):
    soup = BeautifulSoup(page, 'html.parser')

    if 0:
        img2 = soup.select('div #WUCMemberLogin_div_login td #imgCode')
        print(img2)

    if 1:
        results = {}
        results['imgCode'] = soup.find('body').find('div', id = 'WUCMemberLogin_div_login').find('table').find('img', id = 'imgCode')
        # results[target] = soup.find('table').find('tr', id='places_%s__row' % target) \
        #     .find('td', class_="w2p_fw").text
        print(results)



if __name__ == '__main__':

    fgj_url = 'http://fgj.xa.gov.cn/hd/IndexYwzxForum.aspx'

    headers = {
        'User-Agent': r'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      r'Chrome/45.0.2454.85 Safari/537.36 115Browser/6.0.3',
        'Referer': r'http://www.lagou.com/zhaopin/Python/?labelWords=label',
        'Connection': 'keep-alive'
    }
    req = request.Request(fgj_url, headers=headers)
    page = request.urlopen(req).read()
    page = page.decode('utf-8')

    prase_html(page)

