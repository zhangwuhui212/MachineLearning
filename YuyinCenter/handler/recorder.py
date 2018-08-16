#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/2 18:05
# @Author  : zwh
# @Site    : 
# @File    : recorder.py
# @Software: PyCharm

import pyaudio
import wave

class Recorder(object):

    def __init__(self):
        self.CHUNK = 1024
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = 2
        self.RATE = 44100
        self.RECORD_SECONDS = 5
        self.WAVE_OUTPUT_FILENAME = 'local.wav'

        self.engine = pyaudio.PyAudio()

    def record(self):
        try:
            # 提示语句可以使用一下语音方式，这里先打印算了。
            print("Begin Recoding ...")

            stream = self.engine.open(format=self.FORMAT,
                                      channels=self.CHANNELS,
                                      rate=self.RATE,
                                      input=True,
                                      frames_per_buffer=self.CHUNK)
            # 记录到的音频总数据帧
            frames = []
            for i in range(0, int(self.RATE / self.CHUNK * self.RECORD_SECONDS)):
                data = stream.read(self.CHUNK)
                frames.append(data)

            # 音频记录完毕
            print('Recording Over!')
            # 释放资源，接触阻塞监听。
            stream.stop_stream()
            stream.close()
            self.engine.terminate()

            # 并将音频数据保存到本地音频文件中
            wf = wave.open(self.WAVE_OUTPUT_FILENAME, 'wb')
            wf.setnchannels(self.CHANNELS)
            wf.setsampwidth(self.engine.get_sample_size(self.FORMAT))
            wf.setframerate(self.RATE)
            wf.writeframes(b''.join(frames))
            wf.close()
        except Exception as e:
            raise Exception("Recording failed. The reason is {}".format(e))
