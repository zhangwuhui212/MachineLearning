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
        'Cookie':'cookie=58554222; __jsluid=a51ca6a43f38c4941bf1499078e51dc8; ASP.NET_SessionId=rxfgmbuebamguprppudnrzuw; _gscu_422033929=33567331lou7do16; _gscbrs_422033929=1; UM_distinctid=1650fbc7041256-0c0fa8866d33328-516e2220-11bab0-1650fbc70422b1; Hm_lvt_dba247c4516279e648c9ec128654c148=1533567333; CNZZDATA3449008=cnzz_eid%3D140279261-1533566821-http%253A%252F%252Ffgj.xa.gov.cn%252F%26ntime%3D1533566821; Hm_lvt_d7682ab43891c68a00de46e9ce5b76aa=1533567491; Hm_lpvt_d7682ab43891c68a00de46e9ce5b76aa=1533567491; CNZZDATA2851712=cnzz_eid%3D830450983-1533566210-null%26ntime%3D1533598714; _gscs_422033929=t336032250n24py77|pv:2; Hm_lpvt_dba247c4516279e648c9ec128654c148=1533603253'
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
