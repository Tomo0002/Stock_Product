# %%
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression as LR
import joblib
import matplotlib as mpl
from os import read
from numpy.core.fromnumeric import mean
from numpy.lib.function_base import average, select
import pprint
import csv
from pandas.core import construction
from pandas.core.reshape.merge import merge
from pandas.io.parsers import read_csv
from pathlib import Path
from sys import stdin


train = pd.read_csv("D:/Hub/Stock_Product_file/Data.csv",usecols=[2,5])
test = pd.read_csv("D:/Hub/Stock_Product_file/Test.csv", usecols=[2,5])
sample = pd.read_csv("D:/Hub/Stock_Product_file/Sample.csv", header=None)

# print(test.info())
# print(train.info())
train.plot()
plt.show()

# x_train = pd.get_dummies(train)
# y_train = train["y"]

# model = LR()

# model.fit(x_train, y_train)

# model.coef_
# model.intercept_

# train.plot()
# plt.show()