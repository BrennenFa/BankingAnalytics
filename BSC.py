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

df = df[df['CO Amount'].notnull()]
df = df[(df['ProductLine'] == "Home Improvement") | (df['ProductLine'] == "Water") | (df['ProductLine'] == "YellowBlue")]
df = df[df['Late Fees'] !=  '0']
df = df[df['NSF'] != '0']

#Normal data
sns.lmplot(x ="CO Amount", y ="PB BNK", data = df, order = 2, ci = None)
plt.show()


x = np.array(df['PB BNK']).reshape(-1, 1)
y = np.array(df['CO Amount']).reshape(-1, 1)
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size = 0.25)
 
regr = LinearRegression()
 
regr.fit(X_train, y_train)
print(regr.score(X_test, y_test))


#data for repurchased loan status
df1 = df[df['Loan Status'] == 'Repurchased']

sns.lmplot(x ="CO Amount", y ="PB BNK", data = df1, order = 2, ci = None)
plt.show()


x = np.array(df1['PB BNK']).reshape(-1, 1)
y = np.array(df1['CO Amount']).reshape(-1, 1)
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size = 0.25)
 
regr = LinearRegression()
 
regr.fit(X_train, y_train)
print(regr.score(X_test, y_test))




#data for paid loan status
df2 = df[df['Loan Status'] == 'Paid']

sns.lmplot(x ="CO Amount", y ="PB BNK", data = df2, order = 2, ci = None)
plt.show()


x = np.array(df2['PB BNK']).reshape(-1, 1)
y = np.array(df2['CO Amount']).reshape(-1, 1)
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size = 0.25)
 
regr = LinearRegression()
 
regr.fit(X_train, y_train)
print(regr.score(X_test, y_test))


plt.show()

"""
Per our discussion, looking for correlations/factors between charged off loans and the bankruptcy indicator score.

 

These are in columns BK for c/off and Br for bko score.

 

There are some loans that didn’t provide a bko score so those wouldn’t be used in the analysis.


Plan
-organize data categorically
-use plots to see if a correlation exists afterwards

for simplificty
-use home improvement, water, and yellow blue product lines
12500 accounts, 900 will be blank
look at loan status, look at cancelled and refinanced that have a charge off amount
anything w a lender code 20, exclude anything transfered (lender status)
loan population 11475
pb bnk correlated to co amount, columb (bn) and (bm) - late fees and nsf --- fees we cahrge ppl who have been late for their payments

"""