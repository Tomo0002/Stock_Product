import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier

# 出典：「全国の人流オープンデータ」（国土交通省）（https://www.geospatial.jp/ ckan/dataset/mlit-1km-fromto）
df = pd.read_csv("Data\滞在人口データ\兵庫県_滞在人口1_2月.csv")

# メッシュID:28110 神戸市中央区　兵庫県 28 
df_Kobe = df.query('citycode == 28110' and 'timezone == 1')

# メッシュID:28204　西宮市 兵庫県 28 
df_Nisinomiya = df.query('citycode == 28240' and 'timezone == 1')

# メッシュID:28207 伊丹市　兵庫県 28 
df_Itami = df.query('citycode == 28207' and 'timezone == 1')

# メッシュID:28219 三田市　兵庫県 28
df_Sanda = df.query('citycode == 28219' and 'timezone == 1')

# ある行の抽出
# print(df.loc[667,['citycode']])

