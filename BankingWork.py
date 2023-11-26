from scipy.stats import ttest_ind
import pandas as pd
import datetime
import numpy as np
df=pd.read_excel("data.xlsx")


date2023 = np.datetime64('2023-01-01')
df2023 = df[df['Purch Date'] >= date2023]
mean2023 = df2023['Purch Date'].mean()


df.to_csv('data.csv', index=False)



"""
Goals:

Steps
1. Organize data by purchase year
2. Organize data by average
3. Average dq rate by state -> Compare each dealer in state, is it statistically significant
4. Test for normality/decide which test to use


purchase date/year (column P)


 

Some important fields:

 

DQ status (column K)

Dealer info (columns A,B,C)

state (column I)

 

 

Let me know if you have any questions




commands for virtualenv
===================================
python -m venv venv
pip install virtualenv
# In cmd.exe
venv\Scripts\activate.bat


"""