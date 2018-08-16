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

    def buttonListener1(self, event):
        tkinter.filedialog.askopenfile(mode='r', **self.file_opt)
        #tkinter.messagebox.showinfo("messagebox", "this is button 1 dialog")

    def buttonListener2(self, event):
        tkinter.filedialog.asksaveasfile(mode='w', **self.file_opt)

    def buttonListener3(self, event):
        tkinter.filedialog.askdirectory(**self.dir_opt)

    def buttonListener4(self, event):
        tkinter.messagebox.showinfo("messagebox", "this is button 4 dialog")

    def __init__(self):
        self.frame = Tk()

        self.button1 = Button(self.frame, text="select file", width=10, height=5)
        self.button2 = Button(self.frame, text="save file", width=10, height=5)
        self.button3 = Button(self.frame, text="open path", width=10, height=5)
        self.button4 = Button(self.frame, text="button4", width=10, height=5)

        self.button1.grid(row=0, column=0, padx=5, pady=5)
        self.button2.grid(row=0, column=1, padx=5, pady=5)
        self.button3.grid(row=1, column=0, padx=5, pady=5)
        self.button4.grid(row=1, column=1, padx=5, pady=5)

        self.button1.bind("<ButtonRelease-1>", self.buttonListener1)
        self.button2.bind("<ButtonRelease-1>", self.buttonListener2)
        self.button3.bind("<ButtonRelease-1>", self.buttonListener3)
        self.button4.bind("<ButtonRelease-1>", self.buttonListener4)

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