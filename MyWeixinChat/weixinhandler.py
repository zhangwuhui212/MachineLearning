#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/2 17:19
# @Author  : zwh
# @Site    : 
# @File    : weixinhandler.py
# @Software: PyCharm

import itchat

class pyWeixinHandler:

    def __init__(self):
        pass

    def Login(self):
        Wchat = itchat.auto_login(hotReload=True)
        friends = itchat.get_friends()[0:]
        for i in friends:
            print("NickName对应的内容是别人的名字:", i["NickName"])
            print("RemarkName对应的内容是你给别人的备注:", i["RemarkName"])
            print("Signature对应的内容是别人的个性签名:", i["Signature"])
            print("City对应的是别人的城市:", i["City"])
            print("Sex对应的是好友的性别:", i["Sex"])
            input("任意键继续")


    def SendMsg(self):
        Wchat = itchat.auto_login(hotReload=True)
        friends = itchat.get_friends()[1:]

        friend_Uid = ""
        for i in friends:
            if i["RemarkName"] == "老婆":
                # 因为我给我朋友的备注是zr
                print("已经找到了好友的UID哦...")
                friend_Uid = i["UserName"]
                break
        itchat.send_msg("测试", friend_Uid)




if __name__ == '__main__':
	wx = weixinhandler.pyWeixinHandler()
  wx.SendMsg()

