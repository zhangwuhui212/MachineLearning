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
import tkinter.messagebox
import tkinter.filedialog

class MainWindow:

    def __init__(self):
        self.frame = Tk()

        self.lab1 = Label(self.frame, text="username:")
        self.lab2 = Label(self.frame, text="password:")

        self.txt1 = Entry(self.frame)
        self.txt2 = Entry(self.frame)
        var = IntVar()
        self.checkbutton = Checkbutton(self.frame, text='Save password', variable=var)
        self.checkbutton.grid(columnspan=2, sticky=W)

        self.btn = Button(self.frame, text='Fill', width=30)

        self.lab1.grid(row=0, column=0)
        self.lab2.grid(row=1, column=0)
        self.txt1.grid(row=0, column=1)
        self.txt2.grid(row=1, column=1)

        self.checkbutton.grid(row=2, column=0,columnspan=2, sticky=W)
        self.btn.grid(row=3, column=0,columnspan=2, sticky=W+E+N+S, padx=5, pady=5)

        self.frame.mainloop()

window = MainWindow()