#!/usr/bin/env python
# encoding: utf-8
#@version: 0.0.1
#@author: zhangwuhui212
#@license: default 
#@contact: zhangwuhui212@163.com
#@site: 
#@software: PyCharm
#@file: zwhGetVcImageFromUrlImage.py
#@time: 2018/8/9 12:40

'''

本例演示通过webdriver登录网站，保存站点截图，获取验证码截图，解析验证码，模拟登录

注意事项：
    1.安装的 chromedriver和chrome版本需要一致：
        本代码基于：python3.6 ，chrome 68.0.3440.84（正式版本） （32 位），chromedriver2.40
    2.修改：
        C:\Windows\System32\drivers\etc
    下的hosts文件，增加 一行
        127.0.0.1       localhost

    this class login url:
        http://fgj.xa.gov.cn/hd/IndexYwzxForum.aspx
    ok.

'''

import os
import time
import tempfile

from PIL import Image
import pytesseract
from selenium import webdriver


CHROME_DRIVER_PATH = r'C:\\Users\\Administrator\\AppData\\Local\\Google\\Chrome\\Application\\chromedriver.exe'

class mm_zwhGetVcImageFromUrlImage:

    def __init__(self,_url, _auth_code_xpath, _username_ele_id, _password_ele_id, _authcode_ele_id, _login_btn_ele_id):
        self.url = _url
        self.html_auth_code_xpath = _auth_code_xpath
        self.username_ele_id = _username_ele_id
        self.password_ele_id = _password_ele_id
        self.authcode_ele_id = _authcode_ele_id
        self.login_btn_ele_id = _login_btn_ele_id
        self.img_file,self.auth_code_file = self.get_temp_path_map()

    def get_temp_path_map(self):
        temp_path = tempfile.mktemp(prefix='tess_')
        temp_url_image_file = temp_path + os.extsep + "png"
        temp_url_image_frame_file = temp_path + '_frame'+ os.extsep + "png"
        return temp_url_image_file,temp_url_image_frame_file

    def load_driver(self):
        chrome_driver = os.path.abspath(CHROME_DRIVER_PATH)
        driver = webdriver.Chrome(chrome_driver)
        driver.maximize_window()  # 将浏览器最大化
        driver.get(self.url)
        return driver

    def get_auth_code(self, driver, code_element):
        driver.save_screenshot(self.img_file)  # 截取当前网页，该网页有我们需要的验证码
        img_location = code_element.location  # 获取验证码x,y轴坐标
        img_size = code_element.size  # 获取验证码的长宽
        img_rangle = (int(img_location['x']), int(img_location['y']), int(img_location['x'] + img_size['width']),
                     int(img_location['y'] + img_size['height']))
        # 写成我们需要截取的位置坐标
        img = Image.open(self.img_file)  # 打开截图
        img_frame = img.crop(img_rangle)  # 使用Image的crop函数，从截图中再次截取我们需要的区域
        img_frame.save(self.auth_code_file)
        auth_code_img = Image.open(self.auth_code_file)
        auth_code_text = pytesseract.image_to_string(auth_code_img).strip()  # 使用image_to_string识别验证码
        print(auth_code_text)
        return auth_code_text

    def login_web(self, driver, account, passwd, authCode):
        '''登录pandarola系统'''

        driver.find_element_by_id(self.username_ele_id).send_keys(account)
        driver.find_element_by_id(self.password_ele_id).send_keys(passwd)
        driver.find_element_by_id(self.authcode_ele_id).send_keys(authCode)
        driver.find_element_by_id(self.login_btn_ele_id).click()
        time.sleep(2)
        title = driver.find_element_by_id('WUCMemberLogin_lbtnLogOut').text  # 获取登录的标题
        try:
            assert title == u'退出'
            print('登录成功')
        except AssertionError:
            print('登录失败')

    def go(self, username, password):
        driver = self.load_driver()
        code_element = driver.find_element_by_xpath(self.html_auth_code_xpath)  # 定位验证码
        auth_code_text = self.get_auth_code(driver, code_element)
        self.login_web(driver, username, password, auth_code_text)
        time.sleep(1)
        driver.quit()





