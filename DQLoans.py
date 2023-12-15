from scipy.stats import ttest_ind
import pandas as pd
import datetime
import numpy as np
#from statsmodels.stats.weightstats import ztest as ztest
class Methods(object):

    def __init__(self) -> None:
        pass

    #method used to calculate the DQRate
    #returns the average dq rate for a certain factor
    def createDQRate(self, dataFrame):
        dqSum = 0
        num = 0
        for status in dataFrame['DQ Status']:
            #possible errors = if dq is not found, it is not included in number.
            #Is this correct?
            if status.find("Not Found") != -1:
                continue
            if status.find("1") != -1:
                dqSum += 1
            elif status.find("2") != -1:
                dqSum += 1
            elif status.find("3") != -1:
                dqSum += 1
            elif status.find("4") != -1:
                dqSum += 1
            num += 1
        if num == 0:
            return 0
        dqMean2023 = dqSum / num
        return dqMean2023
       

dfData = pd.DataFrame(columns=['Year','State','Dealer','DQ Rate'])

MethodObject = Methods()
df=pd.read_excel("data.xlsx")


date2023 = np.datetime64('2023-01-01')
df2023 = df[df['Purch Date'] >= date2023]

dqRate2023 = MethodObject.createDQRate(df2023)
print("Average DQ Rate for 2023: " + str(dqRate2023))

statesUsed = []
for state in df2023['State']:
    if state in statesUsed:
        continue
    statesUsed.append(state)
    dfState = df2023[(df2023['State'] == state)]
    
    
    dqRatesStateList = []
    dqRateState = MethodObject.createDQRate(dfState)
    
    print("Average DQ Rate for " + state + " in 2023: " + str(dqRateState))
    df2 = pd.DataFrame([(2023, state, "Average", dqRateState)], columns=['Year','State','Dealer','DQ Rate'])
    dfData = dfData._append(df2)
    #Sort by dealer name or dealer id?
    dealersUsed = []
    for dealer in dfState['Dealer Name']:
        if dealer in dealersUsed:
            continue
        dealersUsed.append(dealer)
        dfDealer = dfState[dfState['Dealer Name'] == dealer]

        dqRateDealer = MethodObject.createDQRate(dfDealer)
        print("    Average DQ Rate for " + dealer + " in " + state + " during 2023: " + str(dqRateDealer))
        df2 = pd.DataFrame([(2023, state, dealer, dqRateDealer)], columns=['Year','State','Dealer','DQ Rate'])
        dfData = dfData._append(df2)

        
dfData.to_csv('data.csv', index=False)




#df.to_csv('data.csv', index=False)



"""
Steps completed
1. compute average dq rate for the year 2023
2. computer the average dq rate for each state

Goals:
Steps
1. Organize data by purchase year
2. Organize data by average dq rate per year
3. Average dq rate by state -> Compare each dealer in state, is it statistically significant
4. Test for normality/decide which test to use

one sample z test!

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




"""