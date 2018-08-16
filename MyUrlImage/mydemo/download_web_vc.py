#!/usr/bin/env python
# encoding: utf-8
#@version: 0.0.1
#@author: zhangwuhui212
#@license: default 
#@contact: zhangwuhui212@163.com
#@site: 
#@software: PyCharm
#@file: download_web_vc.py
#@time: 2018/8/6 22:07

import os

image_url_list = [
    'https://vcs.suning.com/vcs/imageCode.htm?uuid=1e68d06a-1134-410b-9606-f0eb4ae23bbe',
    'https://account.flycua.com/sso/chineseVerifyCode.images',
    'http://121.251.136.100/jwxt/sys/ValidateCode.aspx',
    ''
]

def download_vc_1(file_name):
    import urllib
    import pytesseract
    from PIL import Image
    import time

    fp = urllib.request.urlopen(image_url_list[0])
    print(fp)

    f = open(file_name, 'wb')
    f.write(fp.read())
    f.close()

    # fl = open(file_name, 'rb')
    # image = Image.open(fl)
    # image.show()
    #
    # vcode = pytesseract.image_to_string(image)
    # fl.close()
    # print(vcode)

def download_vc_2(file_name):
    import requests

    # 构建session
    sess = requests.Session()
    # 建立请求头
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36",
        "Connection": "keep-alive"}
    # 这个url是联合航空公司验证码，根据访问时间戳返回图片
    url = image_url_list[1]
    # 获取响应图片内容
    image = sess.get(url, headers=headers).content
    # 保存到本地
    with open(file_name, "wb") as f:
        f.write(image)

def download_vc_list(download_callback):
    file_path = os.getcwd() + '\\download_images\\'
    print(file_path)
    no = 0
    while(no < 10):
        file_name = file_path + 'vc_' + str(no) + '.png'
        download_callback(file_name)
        no += 1

if __name__ == '__main__':
    download_vc_list(download_vc_2)
