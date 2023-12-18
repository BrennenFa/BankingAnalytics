import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import preprocessing, svm
from sklearn.model_selection import train_test_split

df=pd.read_excel("BSC_Data.xlsx")
df = df[df['PB BNK'].notnull()]
df = df[df['CO Amount'].notnull()]

df_binary = df[['CO Amount', 'PB BNK']]
 
df_binary.columns = ['CO Amount', 'PB BNK']
sns.lmplot(x ="CO Amount", y ="PB BNK", data = df_binary, order = 2, ci = None)
plt.show()
"""
Per our discussion, looking for correlations/factors between charged off loans and the bankruptcy indicator score.

 

These are in columns BK for c/off and Br for bko score.

 

There are some loans that didn’t provide a bko score so those wouldn’t be used in the analysis.




"""