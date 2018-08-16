#!/usr/bin/env python
# encoding: utf-8
#@version: 0.0.1
#@author: zhangwuhui212
#@license: default 
#@contact: zhangwuhui212@163.com
#@site: 
#@software: PyCharm
#@file: test_pandas.py
#@time: 2018/8/5 13:14

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt


def write_to_csv():
    dates = pd.date_range('20130101', periods=6)
    df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))

    df.to_csv('foo.csv')

def read_from_csv():
    df = pd.read_csv('foo.csv')
    print(df)

def write_to_exl():
    dates = pd.date_range('20130101', periods=6)
    df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))

    df.to_excel('foo.xlsx', sheet_name='Sheet1')

def read_from_exl():
    df =  pd.read_excel('foo.xlsx', 'Sheet1', index_col=None, na_values=['NA'])
    print(df)

if __name__ == '__main__':
    write_to_csv()
    read_from_csv()
