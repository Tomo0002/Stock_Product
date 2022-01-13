from os import terminal_size
import pandas as pd
from scipy.sparse.construct import random

from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier


# 出典：「全国の人流オープンデータ」（国土交通省）（https://www.geospatial.jp/ ckan/dataset/mlit-1km-fromto）
# 「全国の人流オープンデータ」（国土交通省）（https://www.geospatial.jp/ckan/dataset/mlit-1km-fromto）を加工して作成
# メッシュID:28110 神戸市中央区　兵庫県 28 

df = pd.read_csv("Data\売上データ1月.csv", header=1)

arr = df.values

X = arr[:,:3]
y = arr[:,1]

print(y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state= 0)

model = MLPClassifier()

model.fit(X_train, y_train)

print(model.score(X_test, y_test))

# 使用するデータの読み込み 


# ある行の抽出
# print(df.loc[667,['citycode']])

