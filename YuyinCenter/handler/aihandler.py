#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/2 16:54
# @Author  : zwh
# @Site    : 
# @File    : YuyinAIHandler.py
# @Software: PyCharm


#图灵服务器

import string
import json

class YuYinAiHandler:

    def __init__(self):
        self.tuling_key_list = [
            '186cccedc79549ecac4dcc8a56fc9fb4',
            '8edce3ce905a4c1dbb965e6b35c3834d',
            'eb720a8970964f3f855d863d24406576',
            '1107d5601866433dba9599fac1bc0083',
            '71f28bf79c820df10d39b4074345ef8c',
            None
        ]

        self.userid = '产品ID不能说'
        self.url = 'http://www.tuling123.com/openapi/api'



    def AiSay(self,user_say):
        from urllib import request
        from urllib import parse

        api = 'http://www.tuling123.com/openapi/api?key=' + self.tuling_key_list[0] + '&info=' + parse.quote(user_say, safe=string.printable)
        response = request.urlopen(api)
        response_txt = response.read().decode('UTF-8')
        dic_json = json.loads(response_txt)
        return '机器人:' + dic_json['text']


    def AiSay2(self, user_say):
        import requests

        apiUrl = 'http://www.tuling123.com/openapi/api'
        data = {
            'key': self.tuling_key_list[0] ,
            'info': user_say,
            'userid': 'wechat-robot',
        }

        try:
            r = requests.post(apiUrl, data=data).json()
            return r.get('text')
        except:
            # 将会返回一个None
            return
