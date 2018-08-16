#!/usr/bin/env python
# encoding: utf-8
#@version: 0.0.1
#@author: zhangwuhui212
#@license: default 
#@contact: zhangwuhui212@163.com
#@site: 
#@software: PyCharm
#@file: test_dataframe.py
#@time: 2018/8/5 13:25

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def create_dataframe_1():
    dates = pd.date_range('20130101', periods=6)
    #print(dates)

    df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
    print(df)
    #print(df.head())
    #print(df.tail(3))
    # print(df.index)
    # print(df.columns)
    # print(df.values)
    # print(df.describe())
    # print(df.T)#Transposing your data
    # print(df.sort_index(axis=1, ascending=False))#Sorting by an axis
    # print(df.sort_values(by='B'))#Sorting by values:
    #print(df['A'])
    #print(df[0:2])
    print(df.apply(lambda x: x.max() - x.min()))


def create_dataframe_2():
    df = pd.DataFrame({'A': 1.,
                        'B': pd.Timestamp('20130102'),
                        'C': pd.Series(1, index=list(range(4)), dtype='float32'),
                        'D': np.array([3] * 4, dtype='int32'),
                        'E': pd.Categorical(["test", "train", "test", "train"]),
                        'F': 'foo'})
    print(df)

def merge():
    left = pd.DataFrame({'key': ['foo', 'foo'], 'lval': [1, 2]})
    print(left)
    right = pd.DataFrame({'key': ['foo', 'foo'], 'rval': [4, 5]})
    print(right)
    mm = pd.merge(left, right, on='key')
    print(mm)

def merge_1():
    left = pd.DataFrame({'key': ['foo', 'bar'], 'lval': [1, 2]})
    print(left)
    right = pd.DataFrame({'key': ['foo', 'bar'], 'rval': [4, 5]})
    print(right)
    mm = pd.merge(left, right, on='key')
    print(mm)

def Plotting():
    ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
    ts = ts.cumsum()
    ts.plot()
    df = pd.DataFrame(np.random.randn(1000, 4), index=ts.index, columns = ['A', 'B', 'C', 'D'])
    df = df.cumsum()
    plt.figure()
    df.plot()
    plt.legend(loc='best')
    plt.show()

if __name__ == '__main__':
    Plotting()
