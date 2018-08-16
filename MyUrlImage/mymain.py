#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@version: 0.0.1
#@author: zhangwuhui212
#@license: default 
#@contact: zhangwuhui212@163.com
#@site: 
#@software: PyCharm
#@file: mymain.py
#@time: 2018/8/8 11:47

import os
import time
import threading

from zwh_lib.zwhApplication import mm_zwhApplication

from zwh_lib.zwhImageDownloader import mm_zwhImageDownloader

from zwh_lib.zwhImageRecognizer import mm_zwhImageRecognizer

from zwh_lib.zwhHtmlPraser import mm_zwhHtmlPraser
from zwh_lib.zwhHtmlPraser import mm_zwhHtmlPraserMode

from zwh_lib.zwhGetVcImageFromUrlImage import mm_zwhGetVcImageFromUrlImage

from zwh_lib.zwhUrlLoader import mm_zwhUrlLoader

def download_baidu_image():
    ud = mm_zwhUrlLoader(
        'http://image.baidu.com/search/index?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8&word=李沁')
    html = ud.load()

    # print(html)
    hp = mm_zwhHtmlPraser(html, mm_zwhHtmlPraserMode.RE)
    urls = hp.go('"objURL":"(.*?)"')

    print()

    x = 0
    for url in urls:
        x += 1
        print(str(x), url)
        idl = mm_zwhImageDownloader(url, str(x) + '.jpg')
        idl.go()
        if x > 20:  # 设置爬取图片的张数
            break


if __name__ == '__main__':
    savePath = os.path.join(os.getcwd(), 'img_0.png')

    theAPP = mm_zwhApplication()
    theAPP.start()

    #do something

    if 0:
        md = mm_zwhImageDownloader('https://account.flycua.com/sso/chineseVerifyCode.images', savePath)
        md.go_r()

    if 0:
        mr = mm_zwhImageRecognizer(savePath)
        it = mr.image_to_string()
        print(it)

    if 0:
        mgi = mm_zwhGetVcImageFromUrlImage('http://fgj.xa.gov.cn/hd/IndexYwzxForum.aspx',
                                           '//*[@id="imgCode"]',
                                           'WUCMemberLogin_txt_userName',
                                           'WUCMemberLogin_txt_password',
                                           'WUCMemberLogin_txtCheckCode',
                                           'WUCMemberLogin_btn_login')
        mgi.go( 'your username', 'your password')

    if 0:
        hf = open('D:\\fgj.html')
        htl = hf.read()
        hf.close()
        mhp = mm_zwhHtmlPraser(htl)
        rt = mhp.go('//*[@id="form1"]/div[5]/div[1]//option/text()')
        print(rt)


    if 1:
        download_baidu_image()

    theAPP.stop()
