#%%
import matplotlib.pyplot as plt
import matplotlib as mpl
from os import read
from numpy.core.fromnumeric import mean
from numpy.lib.function_base import average, select
import pandas as pd
import numpy as np
import math
import pprint
import csv
from pandas.core import construction
from pandas.io.parsers import read_csv
from pathlib import Path
from sys import stdin
 
# header = 0で各項目の題名を取得する　確認方法print(df.head(3))で項目が出力されるかどうか
df = pd.read_csv("", header= 0)
# df = pd.DataFrame(data=df)
# print(df.head(3))
# print(df.columns)

# 読み込む列を指定
# df = pd.read_csv("D:\All Code File\Python\Excel Date List\安定在庫量.csv", usecols=[0,2])
# print(df)

# 条件指定・抽出
# print(df[df["Number_Of_Stock"] > 100])

# 日付・個数の抽出
# date = df["Date"][0]
# salle = df["Number_Of_Sales"][0]
# str_datesalle = f'{date} {salle}個'
# print(str_datesalle)

# 条件分岐
Stocksituation = [
    (df["Number_Of_Stock"] == 0),
    (df["Number_Of_Stock"] < 24),
    (df["Number_Of_Stock"] >= 24) & (df["Number_Of_Stock"] <= 72),
    (df["Number_Of_Stock"] >= 72)   
 ]

choicelist = ['Out_Of_Stock','order', 'attention', 'safe',]
df["Stock_Status"] = np.select(Stocksituation, choicelist, default="Non")
print(df)
print("--------------------------------------------------------")

# 計算
Sum_Sales = sum(df["Number_Of_Sales"])
print(f"売上個数:{Sum_Sales}")

Max_Sale = max(df["Number_Of_Sales"])
print(f"最高販売数:{Max_Sale}")

Ave_Sales = average(df["Number_Of_Sales"])
print(f"平均売上個数{Ave_Sales.round(2)}")

# CSVに出力
# df.to_csv("D:\\All Code File\\Python\\Excel Date List\\安定在庫量.csv")


# 結果を四捨五入する
# print(data.describe().round(2))





