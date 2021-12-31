# %%
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression as LR
from sklearn import linear_model
import joblib
import matplotlib as mpl
from numpy.core.fromnumeric import mean
import pprint
import csv
from pandas.io.parsers import read_csv
from pathlib import Path
from sys import stdin


df_x = read_csv("Data\売上データ.csv", usecols=[1, 2], encoding='utf-8')
df_y = read_csv("Data\Test.csv", usecols=[1, 2], encoding='utf-8')

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
model = linear_model.LinearRegression()

# 当てはめるデータ
x = df_x.loc[:,["売上個数", "最高気温"]].values
y = df_y["最高気温"].values

# 予測
# X2 = [[df_x] for x in df_x]

model.fit(x, y)

a = model.coef_
b = model.intercept_

# グラフを表示する場合
print("回帰係数:" , a)
print("切片: ", b)
print("決定係数: ", model.score(x, y))

# グラフを表示せず結果のみ知りたい場合
# print("回帰係数:" , clf.coef_)
# print("切片: ", clf.intercept_)
# print("決定係数: ", clf.score(x, y))

# 棒グラフ
# df_x.plot(kind='bar')
# df_y.plot(kind='bar')

# メモリの範囲指定
# plt.xlim(0, 50)
# plt.ylim(0,50)

# 散布図
plt.scatter(df_x, df_y , color="blue")

# 回帰直線
plt.plot(df_x,(a* df_x + b), color="green")


plt.show()

