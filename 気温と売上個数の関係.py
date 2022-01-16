#%%
import pandas as pd

import matplotlib.pyplot as plt

from sklearn import linear_model


df_x = pd.read_csv("Data\売上データ全体.csv", usecols=[1, 2], encoding='utf-8')
df_y = pd.read_csv("Data\Test.csv", usecols=[1, 2], encoding='utf-8')

# データ数カウント
# print(df_y.shape)
# print(df_x.shape)

# 欠損値確認
# print(df_x.isnull().sum())
# print(df_y.isnull().sum())

#  項目値
# print(df_x.describe)
# print(df_y.describe)

# モデル
model = linear_model.LinearRegression()

x = df_x.loc[:, ["売上個数", "最高気温"]].values
y = df_y["売上個数"].values

model.fit(x, y)

# a = model.coef_
# b = model.intercept_
# df_corr = df_x.corr()

print("回帰係数:" , model.coef_)
print("切片: ", model.intercept_)
print("決定係数: ", model.score(x, y))
print("相関係数: ",df_corr)

plt.scatter(df_x, df_y, color="blue")

plt.title("Relationship between temperature and sales quantity")

plt.show()