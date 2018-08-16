#!/usr/bin/env python
# encoding: utf-8
#@version: 0.0.1
#@author: zhangwuhui212
#@license: default 
#@contact: zhangwuhui212@163.com
#@site: 
#@software: PyCharm
#@file: zwhHtmlPraser.py
#@time: 2018/8/8 16:12 

from lxml import etree
from lxml.etree import ParseError

import re

class mm_zwhHtmlPraserMode:
    RE = "re"
    XP = "xpath"

class mm_zwhHtmlPraser:
    def __init__(self,_html,_mode = mm_zwhHtmlPraserMode.XP):
        self.html = _html
        self.mode = _mode

    def go(self,pstr):
        result = ''
        try:
            if self.mode == mm_zwhHtmlPraserMode.XP:
                html_obj = etree.HTML(self.html, etree.HTMLParser())
                result = html_obj.xpath(pstr)
            else:
                result = re.findall(pstr, self.html, re.S)
        except ParseError as e:
            print(e.position)
        return result

if __name__ == '__main__':
    pass
