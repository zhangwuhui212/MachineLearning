#!/usr/bin/env python
# encoding: utf-8
#@version: 0.0.1
#@author: zhangwuhui212
#@license: default 
#@contact: zhangwuhui212@163.com
#@site: 
#@software: PyCharm
#@file: zwhApplication.py
#@time: 2018/8/8 11:49


import os

import threading

from zwhConfig import mm_zwhConfig
from zwhMainThread import mm_zwhMainThread

class mm_zwhApplication:
    def __init__(self, _logpath='', _logname='sample.txt'):
        self.logpath = os.path.join(_logpath,_logname)
        self.logfile = open(self.logpath,'wb')

        self.cfg = mm_zwhConfig()

        self.threadid = 0
        self.exitFlag = threading.Event()
        self.mainthread = mm_zwhMainThread(self.new_threadid(), 'zwhAppMainThread',self.exitFlag)

    def __del__(self):
        #print("app_del")
        self.logfile.close()
        os.remove(self.logpath)

    def new_threadid(self):
        self.threadid += 1
        return self.threadid

    def del_threadid(self):
        if self.threadid > 0:
            self.threadid -= 1


    def start(self):
        self.mainthread.start()

    def stop(self):
        self.exitFlag.set()
        self.mainthread.join()
        #print('app_stop')

