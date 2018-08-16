#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/2 18:22
# @Author  : zwh
# @Site    : 
# @File    : vcr.py
# @Software: PyCharm

from PIL import Image
import pytesseract


def show_pic(pic):
    img = Image.open(pic)
    img.show()

def show_pic2(pic):
    from PIL import Image
    import matplotlib.pyplot as plt
    img = Image.open(pic)
    plt.figure("dog")
    plt.imshow(img)
    plt.show()

def vc_pic(pic):
    img = Image.open(pic)
    aa = pytesseract.image_to_string(img,lang='chi_sim')
    print(aa)

if __name__ == '__main__':
    print('ok')

    #vc_pic('D:\\MyCode\\vc_pic\\eng_1.png')
    #vc_pic('D:\\MyCode\\vc_pic\\ch_1.png')
    #vc_pic('D:\\MyCode\\vc_pic\\ch_2.png')

