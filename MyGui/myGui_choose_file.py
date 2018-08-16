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

    def buttonOpenFile(self, event):
        path = tkinter.filedialog.askopenfile(mode='r', **self.file_opt)
        self.file_path.set(path.name)

    def buttonShibie(self, event):
        print('start shibie...')

    def __init__(self):
        self.frame = Tk()

        self.file_lab = Label(self.frame, text="file:")

        self.file_path = StringVar()
        self.file_txt = Entry(self.frame, width=30, textvariable= self.file_path,state="readonly")
        self.button1 = Button(self.frame, text="select file", width=10, height=1)
        self.button2 = Button(self.frame, text="start shibie", width=10, height=1)

        self.file_lab.grid(row=0, column=0)
        self.file_txt.grid(row=0, column=1)
        self.button1.grid(row=0, column=2)
        self.button2.grid(row=1, column=0,columnspan=3, sticky=W+E+N+S, padx=5, pady=5)

        self.button1.bind("<ButtonRelease-1>", self.buttonOpenFile)
        self.button2.bind("<ButtonRelease-1>", self.buttonShibie)

        self.file_opt = options = {}
        options['defaultextension'] = '.txt'
        options['filetypes'] = [('all files', '.*'), ('text files', '.txt')]
        options['initialdir'] = 'C:\\'
        options['initialfile'] = 'myfile.txt'
        options['parent'] = self.frame
        options['title'] = 'This is a title'

        self.dir_opt = options = {}
        options['initialdir'] = 'C:\\'
        options['mustexist'] = False
        options['parent'] = self.frame
        options['title'] = 'This is a title'

        self.frame.mainloop()


window = MainWindow()