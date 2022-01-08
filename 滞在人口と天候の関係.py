import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier

# メッシュID:28110 兵庫県 28 神戸市中央区	兵庫県神戸市中央区
# 出典：「全国の人流オープンデータ」（国土交通省）（https://www.geospatial.jp/ ckan/dataset/mlit-1km-fromto）
df = pd.read_csv("滞在人口データ\兵庫県_滞在人口1_2月.csv")
print(df)
