#!/usr/bin/env python
# encoding: utf-8
#@version: 0.0.1
#@author: zhangwuhui212
#@license: default 
#@contact: zhangwuhui212@163.com
#@site: 
#@software: PyCharm
#@file: test_series.py
#@time: 2018/8/5 13:17 

import numpy as np
import pandas as pd


def from_ndarray():
    s = pd.Series(np.random.randn(5), index=['a', 'b', 'c', 'd', 'e'])
    #print(s)
    #print(s.index)
    print(s)
    s = pd.Series(np.random.randn(5))
    print(s)

def from_dict():
    d = {'b': 1, 'a': 0, 'c': 2}
    s = pd.Series(d)
    print(s)
    s = pd.Series(d, index=['b', 'c', 'd', 'a'])
    print(s)


if __name__ == '__main__':
    #from_ndarray()
    from_dict()
