import pandas as pd
import datetime as dt
from pandas_datareader import data as pdr
import yfinance as yf
import plotly.express as px
import matplotlib.pyplot as plt

yf.pdr_override()
#pd.options.plotting.backend = "plotly"


#create range of time for which you want to extract data (year, month, day)
startDate = dt.datetime(2000, 1, 1)
endDate = dt.datetime(2020, 12, 31)

#List of stock tickers for their data to be extracted
stockList = ['AAPL', 'GOEV']

#uses function get_data_yahoo to extract the specified data into a data fram object for further manipulation
df = pdr.get_data_yahoo(stockList, startDate, endDate)

#print the 1st 5 rows
print(df.head())

#print(df.index)
#print(df.columns)
#Close = df.Close
#print(Close.head())
#print(Close.describe())
#Close.plot()
#plt.show()


