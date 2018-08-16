#!/usr/bin/env python
# encoding: utf-8
#@version: 0.0.1
#@author: zhangwuhui212
#@license: default 
#@contact: zhangwuhui212@163.com
#@site: 
#@software: PyCharm
#@file: test_xml.py
#@time: 2018/8/7 14:31

#http://www.cnblogs.com/zhangxinqi/p/9210211.html

import requests
from requests.exceptions import RequestException

from lxml import etree
from lxml.etree import ParseError
import json


def one_to_page(html):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36'
    }
    try:
        response = requests.get(html, headers=headers)
        body = response.text  # 获取网页内容
    except RequestException as e:
        print('request is error!', e)
    try:
        html  = etree.HTML(body, etree.HTMLParser())  # 解析HTML文本内容
        result = html.xpath('//table[contains(@class,"table-top20")]/tbody/tr//text()')  # 获取列表数据
        pos = 0
        for i in range(20):
            if i == 0:
                yield result[i:5]
            else:
                yield result[pos:pos + 5]  # 返回排名生成器数据
            pos += 5
    except ParseError as e:
        print(e.position)

def load_html_file(ff):
    html_f = open(ff,'rb')
    html_txt = html_f.read()
    #print(html_txt)
    html_f.close()
    try:
        html = etree.HTML(html_txt, etree.HTMLParser())
        #result = html.xpath('//*')#//代表获取子孙节点，*代表获取所有
        result = html.xpath('//tr')#获取所有子孙节点的tr节点
        result = html.xpath('//tr/td')  # 通过追加/a选择所有li节点的所有直接a节点，因为//li用于选中所有li节点，/a用于选中li节点的所有直接子节点a
        #result = html.xpath('//tr/../@class')#获取父节点

        #属性匹配
        #选取class为table-top20的table节点
        #result = html.xpath('//table[@class="table-top20"]')

        #文本获取
        result = html.xpath('//table[@class="table-top20"]/tr/td/text()')  # 获取a节点下的内容

        #属性获取
        #result = html.xpath('//tr/td/@align')  # 获取td的href属性

        #属性多值匹配
        #如果某个属性的值有多个时，我们可以使用contains()函数来获取
        #result = html.xpath('//td[contains(@class,"aaa")]/text()')

        #多属性匹配
        #result = html.xpath('//td[contains(@class,"aaa") and @name="123"]/text()')

        rd = []
        i = 0
        # for i in range(result.size):
        #     rd[result[i]:result[i+3]]
        #     i += 3
        print(result)
    except ParseError as e:
        print(e.position)

    return result


def write_file(data):  # 将数据重新组合成字典写入文件并输出
    for i in data:
        sul = {
            '语言': i[0],
            # '2018年8排行': i[1],
            # '2017年9排行': i[2]
        }
        with open('test.txt', 'a', encoding='utf-8') as f:
            f.write(json.dumps(sul, ensure_ascii=False) + '\n')  # 必须格式化数据
            f.close()
        print(sul)
    return None


def main():
    url = 'https://www.cnbeta.com/articles/tech/754559.htm'
    #data = one_to_page(url)

    data = load_html_file('c_bc.txt')
    revaule = write_file(data)
    # if revaule == None:
    #     print('ok')


if __name__ == '__main__':
    main()
