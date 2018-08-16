#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/3 12:58
# @Author  : zwh
# @Site    : 
# @File    : vcr2.py
# @Software: PyCharm

#测试成功

from PIL import Image
import pytesseract

import PIL.ImageOps
import PIL.ImageEnhance

def show_pic(pic):
    img = Image.open(pic)
    img.show()

def initTable(threshold=140):
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)
    return table

def vc_pic_1(pic):
    img = Image.open(pic)
    aa = pytesseract.image_to_string(img)
    print(aa)

def vc_pic(pic):
    im = Image.open(pic)

    im = im.convert('L')#将RGB彩图转为灰度图
    binaryImage = im.point(initTable(), '1')#将灰度图按照设定阈值转化为二值图


    im1 = binaryImage.convert('L')

    im2 = PIL.ImageOps.invert(im1)

    im3 = im2.convert('1')

    im4 = im3.convert('L')
    # 将图片中字符裁剪保留
    #print(im4.size)
    #左 下 上 右
    box = (5, 2, im4.size[0]-1, im4.size[1]-1)
    region = im4.crop(box)
    # 将图片字符放大
    out = region.resize((120, 38))
    #out.show()
    asd = pytesseract.image_to_string(out)
    print(asd)


if __name__ == '__main__':
    print('ok')
    vc_pic('vc.png')
    #vc_pic('.\\vc\\1.png')
    #vc_pic('.\\vc\\2.png')
    #vc_pic('.\\vc\\3.png')
    #vc_pic('.\\vc\\4.png')
