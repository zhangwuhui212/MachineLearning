#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/2 17:49
# @Author  : zwh
# @Site    : 
# @File    : baiduhandler.py
# @Software: PyCharm

import pyaudio
import wave
import requests
import json

class useBaiduHandler:

    def __init__(self):
        # get the token
        self.token = self.gettoken()

    def gettoken(self):
        try:
            apiKey = "BElGG5nsGL8oevAa3gMzMk4Y"
            secretKey = "uVla1FdpQ2HgmojeY9e6pobrS3lRGaeY"

            auth_url = "https://openapi.baidu.com/oauth/2.0/token?grant_type=client_credentials&client_id=" + apiKey + "&client_secret=" + secretKey
            response = requests.get(url=auth_url)
            jsondata = response.text
            return json.loads(jsondata)['access_token']
        except Exception as e:
            raise Exception("Cannot get the token, the reason is {}".format(e))

    def parse(self, wavefile='16k.wav'):
        try:
            fp = wave.open(wavefile, 'rb')
            # 已经录好音的音频片段内容
            nframes = fp.getnframes()
            filelength = nframes * 2
            audiodata = fp.readframes(nframes)

            # 百度语音接口的产品ID
            cuid = '7519663'
            server_url = 'http://vop.baidu.com/server_api' + '?cuid={}&token={}'.format(cuid, self.token)
            headers = {
                'Content-Type': 'audio/pcm; rete=8000',
                'Content-Length': '{}'.format(filelength),
            }

            response = requests.post(url=server_url, headers=headers, data=audiodata)
            print(response.text)
            data = json.loads(response.text)
            if data['err_msg'] == 'success.':
                return data['result']
            else:
                return '你说的啥啊，听不清听不清！'
        except Exception as e:
            raise Exception("Parsing wave file failed. The reason is {}".format(e))
