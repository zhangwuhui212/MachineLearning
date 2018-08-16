#!/usr/bin/env python
# encoding: utf-8
#@version: 0.0.1
#@author: zhangwuhui212
#@license: default 
#@contact: zhangwuhui212@163.com
#@site: 
#@software: PyCharm
#@file: zwhImageRecognizer.py
#@time: 2018/8/8 14:20 

import os
import PIL
import PIL.ImageOps
import pytesseract

import tempfile
from os.path import realpath, normpath, normcase

import subprocess

tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
tesseract_tessdata_path = r'C:\\Program Files\\Tesseract-OCR\\tessdata'
tesseract_tessdata_config = '--tessdata-dir "C:\\Program Files\\Tesseract-OCR\\tessdata"'


class Output:
    STRING = "string"
    BYTES = "bytes"
    DICT = "dict"


class TesseractNotFoundError(EnvironmentError):
    def __init__(self):
        super(TesseractNotFoundError, self).__init__(
            tesseract_cmd + " is not installed or it's not in your path"
        )

class TesseractError(RuntimeError):
    def __init__(self, status, message):
        self.status = status
        self.message = message
        self.args = (status, message)

class mm_zwhImageRecognizer:

    def __init__(self,_imgfile):
        self.imgfile = _imgfile
        self.hdtable = self.initTable()

    def image_to_string(self):
        img_txt = ''
        img = PIL.Image.open(self.imgfile)
        img_txt = pytesseract.image_to_string(img)
        return img_txt


    def initTable(self,threshold=140):
        table = []
        for i in range(256):
            if i < threshold:
                table.append(0)
            else:
                table.append(1)
        return table

    def image_to_string_mm(self):
        im = PIL.Image.open(self.imgfile)
        im = im.convert('L')# 将RGB彩图转为灰度图
        binaryImage = im.point(self.hdtable, '1')# 将灰度图按照设定阈值转化为二值图
        im1 = binaryImage.convert('L')
        im2 = PIL.ImageOps.invert(im1)
        im3 = im2.convert('1')
        im4 = im3.convert('L')
        # 将图片中字符裁剪保留
        # print(im4.size)
        # 左 下 上 右
        box = (5, 2, im4.size[0] - 1, im4.size[1] - 1)
        region = im4.crop(box)
        # 将图片字符放大
        out = region.resize((120, 38))
        # out.show()
        img_txt = pytesseract.image_to_string(out)
        return img_txt

    def image_to_string_run(self):
        temp_name = tempfile.mktemp(prefix='tess_') + '_out'
        out_name = temp_name + os.extsep + 'txt'
        print(temp_name,'\r\n',out_name)
        cmd_args = [tesseract_cmd, self.imgfile, temp_name, '--tessdata-dir',tesseract_tessdata_path,'-l','chi_sim']

        kwargs = {
            'stdin': subprocess.PIPE,
            'stderr': subprocess.PIPE,
            'startupinfo': None,
            'env': None
        }

        try:
            proc = subprocess.Popen(cmd_args, **kwargs)
        except OSError:
            raise TesseractNotFoundError()

        status_code, error_string = proc.wait(), proc.stderr.read()
        proc.stderr.close()
        print(status_code, error_string)

        with open(out_name, 'rb') as output_file:
            img_txt = output_file.read().decode('utf-8').strip()
            return img_txt






