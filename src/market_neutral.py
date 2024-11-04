import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#create filepath for excel file
filepath = 'C:\\Users\\rhyth\\OneDrive\\Desktop\\Trading\\Python codes\\IGE.xls'

#read entire excel file into a dataframe
df = pd.read_excel(filepath)

#sort the data frame by the 'Date' column and update the currennt dataframe, df
#by default this is in asending order, first row will have oldest date and last row will have most recent date
df.sort_values(by='Date', inplace=True)

#select all the rows of the 'Adj Close' column
adjCloseColumn = df.loc[:, 'Adj Close']

#new column(same length as previous column) where an arbitrary row m is the % change from the m-1 row to the m row (in adjCloseColumn)
#first row will be NaN since there is no row before it
#each row will be the (daily) return from one date to the next (in terms of a %)
dailyret = adjCloseColumn.pct_change()

#excess returns based on a 4% risk free rate and 252 trading days per year
#the last term is converting the average yearly risk free rate to the average daily risk free rate. This is neccissary since we are dealing with DAILY returns
excessRet = dailyret - 0.04/252

#sharpe ratio
sharpeRatio = np.mean(excessRet) / np.std(excessRet)
annualizedSharpeRatio = np.sqrt(252) * sharpeRatio
#print(annualizedSharpeRatio)



#part 2
#long/short market nutral 

#create filepath
filepath = 'C:\\Users\\rhyth\\OneDrive\\Desktop\\Trading\\Python codes\\SPY.xls'

#read in excel file into a new dataframe
df2 = pd.read_excel(filepath)

#"update" df to be the combination of df and df2 with their "Date" coulumns aligned
#df is the merged dataframe
df = pd.merge(df, df2, on= 'Date', suffixes= ('_IGE', '_SPY'))

#update the "Date" coulumn to make sure the objects in each row is a datetime object
df['Date'] = pd.to_datetime(df['Date'])

#set the index of df to be the date coulumn
#the column is no longer a regualar column
#inplace=true to modify df directly
df.set_index('Date', inplace= True)

#sort the df by index, which is now the date coulumn< in assending order(chronological, which is the default)
df.sort_index(inplace= True)

#new dataframe that contains the daily return (in %) of IGE and SPY over the time interval
dailyret2 = df[['Adj Close_IGE', 'Adj Close_SPY']].pct_change() 

#rename the coulumns of dailyret2
dailyret2.rename(columns={"Adj Close_IGE" : "IGE", "Adj Close_SPY" : "SPY"}, inplace=True)


netRet = (dailyret2['IGE'] - dailyret2['SPY']) / 2


sharpeRatio2 = np.sqrt(252) * np.mean(netRet) / np.std(netRet)
#print(sharpeRatio2)




#drawdowns

cumret = np.cumprod(1 + netRet) - 1
plt.plot(cumret)
plt.show()
from calculateMaxDD import calculateMaxDD
maxDrawdown , maxDrawdownDuration, startDrawdownDay = calculateMaxDD(cumret.values)
print(maxDrawdown)
print(maxDrawdownDuration)
print(startDrawdownDay)






