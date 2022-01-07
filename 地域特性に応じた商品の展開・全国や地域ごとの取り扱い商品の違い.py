# from __future__ import print_function

from functools import cached_property
import pandas as pd
from pandas import Series,DataFrame

from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LinearRegression


import numpy as np
import matplotlib.pyplot as plt
# %matplotlib.inline

import keras
from keras.datasets import fashion_mnist
from keras.models import Sequential, Model
from keras.layers import Input, Dense, Dropout


# (C) ウレコンpowered by TRUE DATA

# データ取り込み
df_1 = pd.read_csv("ウレコン\ウレコン_関西_お茶ペットボトル飲料シェア.csv")
# df_2 = pd.read_csv("ウレコン\ウレコン_全国_お茶ペットボトル飲料シェア.csv", usecols=[0,1,2,3,4]) 

x = DataFrame(df_1.drop(["にごり"], axis =1))
y = DataFrame(df_1[["にごり","急須", "ブレンド","旨味"]])

x_train,x_test,y_train,y_test =train_test_split(x, y, test_size=0.05)

#データの整形
x_train = x_train.astype
x_test = x_test.astype





# url= "https://qiita.com/tanakadaichi_1989/items/c655d93a1fae56f2be07"
# url = "https://qiita.com/takahiro_itazuri/items/d2bea1c643d7cca11352"