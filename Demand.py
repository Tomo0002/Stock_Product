import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression as LR
# %matplotlib inline

train = pd.read_csv("D:/Hub/Stock_Product_file/Data.csv", header=0)
test = pd.read_csv("D:/Hub/Stock_Product_file/Hyogo_Temle_data.csv")
sample = pd.read_csv("D:/Hub/Stock_Product_file/Sample.csv")

print(test.info())