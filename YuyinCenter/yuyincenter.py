#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/2 14:29
# @Author  : zwh
# @Site    : 
# @File    : yuyincenter.py
# @Software: PyCharm


from Common import aihandler 



if __name__ == '__main__':
    print("YuyinCenter runninig...") 
    AI = aihandler.YuYinAiHandler()

    ai_say = AI.AiSay2("你好!")
    print(ai_say) 

    exit(0)

