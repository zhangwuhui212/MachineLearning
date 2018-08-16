#!/usr/bin/env python
# encoding: utf-8
#@version: 0.0.1
#@author: zhangwuhui212
#@license: default 
#@contact: zhangwuhui212@163.com
#@site: 
#@software: PyCharm
#@file: zwhMainThread.py
#@time: 2018/8/8 12:59

import time
import threading

class mm_zwhMainThread(threading.Thread):

    def __init__(self, threadID, name, exitFlag):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.exitFlag = exitFlag

    def run(self):  # 把要执行的代码写到run函数里面 线程在创建后会直接运行run函数
        print("Starting " + self.name)
        while not self.exitFlag.isSet():
            #print('mm_zwhMainThread is running...')
            time.sleep(2)
        print("Exiting " + self.name)


if __name__ == '__main__':
    pass
