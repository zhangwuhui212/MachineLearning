#!/usr/bin/env python
# encoding: utf-8
#@version: 0.0.1
#@author: zhangwuhui212
#@license: default 
#@contact: zhangwuhui212@163.com
#@site: 
#@software: PyCharm
#@file: myGui.py
#@time: 2018/8/15 14:45 


from tkinter import *
import time

'''
定义消息发送函数：
1、在<消息列表分区>的文本控件中实时添加时间；
2、获取<发送消息分区>的文本内容，添加到列表分区的文本中；
3、将<发送消息分区>的文本内容清空。
'''


def msgsend():
    msg = '我' + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()) + '\n'
    txt_msglist.insert(END, msg, 'green')  # 添加时间
    txt_msglist.insert(END, txt_msgsend.get('0.0', END))  # 获取发送消息，添加文本到消息列表
    txt_msgsend.delete('0.0', END)  # 清空发送消息


'''定义取消发送 消息 函数'''


def cancel():
    txt_msgsend.delete('0.0', END)  # 取消发送消息，即清空发送消息


'''绑定up键'''


def msgsendEvent(event):
    if event.keysym == 'Up':
        msgsend()


tk = Tk()
tk.title('聊天窗口')

'''创建分区'''
f_msglist = Frame(height=300, width=300)  # 创建<消息列表分区 >
f_msgsend = Frame(height=300, width=300)  # 创建<发送消息分区 >
f_floor = Frame(height=100, width=300)  # 创建<按钮分区>
f_right = Frame(height=700, width=100)  # 创建<图片分区>

'''创建控件'''
txt_msglist = Text(f_msglist)  # 消息列表分区中创建文本控件
txt_msglist.tag_config('green', foreground='blue')  # 消息列表分区中创建标签
txt_msgsend = Text(f_msgsend)  # 发送消息分区中创建文本控件
txt_msgsend.bind('<KeyPress-Up>', msgsendEvent)  # 发送消息分区中，绑定‘UP’键与消息发送。
'''txt_right = Text(f_right) #图片显示分区创建文本控件'''
button_send = Button(f_floor, text='Send', command=msgsend)  # 按钮分区中创建按钮并绑定发送消息函数
button_cancel = Button(f_floor, text='Cancel', command=cancel)  # 分区中创建取消按钮并绑定取消函数
photo = PhotoImage(file=r'my.gif')
label = Label(f_right, image=photo)  # 右侧分区中添加标签（绑定图片）
label.image = photo

'''分区布局'''
f_msglist.grid(row=0, column=0)  # 消息列表分区
f_msgsend.grid(row=1, column=0)  # 发送消息分区
f_floor.grid(row=2, column=0)  # 按钮分区
f_right.grid(row=0, column=1, rowspan=3)  # 图片显示分区
txt_msglist.grid()  # 消息列表文本控件加载
txt_msgsend.grid()  # 消息发送文本控件加载
button_send.grid(row=0, column=0, sticky=W)  # 发送按钮控件加载
button_cancel.grid(row=0, column=1, sticky=W)  # 取消按钮控件加载
label.grid()  # 右侧分区加载标签控件

tk.mainloop()
