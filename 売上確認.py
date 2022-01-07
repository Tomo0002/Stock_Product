import pandas as pd

import numpy as np
from numpy.lib.function_base import average, select
from pandas.io.parsers import read_csv

import datetime
import requests
import io

import datetime


# データ取得
df = pd.read_csv("Data\売上データ.csv")

# 気象データを取得　(作成中)
# url = "https://www.data.jma.go.jp/obd/stats/data/mdrr/tem_rct/alltable/mxtemsadext00_rct.csv"
# r = requests.get(url).content
# df_1 = pd.read_csv(io.BytesIO(r), sep = ";")
# ↑　https://ibuki-study.net/csv_from_url_by_python/


# 条件指定・抽出
# print(df[df["Number_Of_Stock"] > 100])

# 条件分岐
# Stocksituation = [
#     (df["在庫量"] == 0),
#     (df["在庫量"] < 24),
#     (df["在庫量"] >= 24) & (df["在庫量"] <= 72),
#     (df["在庫量"] >= 72)   
# ]

# choicelist = ['欠品','注文', '注意', '安全']
# df["Stock_Status"] = np.select(Stocksituation, choicelist, default="Non")

print(df)

print("--------------------------------------------------------")

print(f"更新時間: {datetime.datetime.now()}")

# 気象データ (作成中)
# print(df_1)
# Ave_Max_Temple_Osa_Des = average(df_temperature_Osa["最高気温"])
# print(f"12月の大阪平均気温(最高){Ave_Max_Temple_Osa_Des.round(2)}℃")

# 計算
Sum_Sales = sum(df["売上個数"])
print(f"売上個数:{Sum_Sales}個")

Max_Sale = max(df["売上個数"])
print(f"最高販売数:{Max_Sale}個")

Ave_Sales = average(df["売上個数"])
print(f"平均売上個数{Ave_Sales.round(2)}個")

# CSVに出力
# df.to_csv("Sample.csv", encoding = "utf-8")




