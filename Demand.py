# %%
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression as LR
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn import linear_model
import joblib
import matplotlib as mpl
from os import read
from numpy.core.fromnumeric import mean
from numpy.lib.function_base import average, select
import pprint
import csv
import math
from pandas.core import construction
from pandas.core.reshape.merge import merge
from pandas.io.parsers import read_csv
from pathlib import Path
from sys import stdin
import datetime



def main():
    df_x = read_csv("Data\Data.csv", usecols=[1,4])
    df_y = read_csv("Data\Test.csv", usecols=[1,4])

# データ確認
# print(df_x)
# print(df_y)

# データ数カウント
# print(df_y.shape)
# print(df_x.shape)

# 欠損値確認
# print(df_x.isnull().sum())
# print(df_y.isnull().sum())

# 項目値
# print(df_x.describe)
# print(df_y.describe)

# numpyに変換
# arr = df_x.values
# arr = df_y.values
# print(type(arr))

    # モデル
    clf = linear_model.LinearRegression()

    # 当てはめるデータ
    x = df_x.loc[:, ["Highes_Temperature", "Number_Of_Sales"]].values
    y = df_y["Number_Of_Sales"].values

# 予測
# X2 = [[df_x] for x in df_x]


    clf.fit(x, y)

    a = clf.coef_
    b = clf.intercept_

    # グラフを表示する場合
    print("回帰係数:" , a)
    print("切片: ", b)
    print("決定係数: ", clf.score(x, y))
    
    # グラフを表示せず結果のみ知りたい場合
    # print("回帰係数:" , clf.coef_)
    # print("切片: ", clf.intercept_)
    # print("決定係数: ", clf.score(x, y))
    
    # 棒グラフ
    # df_x.plot(kind='bar')
    # df_y.plot(kind='bar')
    # plt.show()
    
    
    # 日付を入れる場合
    # sxmin = '2021-11-1'
    # sxmax = "2021-11-30"
    # xmin = datetime.datetime.strptime(sxmin,'%Y-%m-%d')
    # xmax = datetime.datetime.strptime(sxmax, '%Y-%m-%d')
    # plt.xlim([xmin, xmax])
    
    # メモリの範囲指定
    plt.xlim(0, 50)
    plt.ylim(0,50)
    
    # 散布図
    plt.scatter(df_x, df_y , color="blue")
    
    # 回帰直線
    # plt.plot(df_x,(a* df_x + b), color="green")
    
    
    plt.show()
    
 
if __name__ == "__main__": main()