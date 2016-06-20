# -*- coding: utf-8 -*-
"""
Created on Sat May 14 17:23:46 2016

@author: keith
"""

import datetime

from yahoo_finance import Share

class FinancialData:
  def __init__(self, date):
    self.date = date

    # initialize the S&P500 Data


start_date = '2015-06-01'
end_date = datetime.datetime.now().strftime("%Y-%m-%d")

print "Processing from %s to %s\n"%(start_date, end_date)

# get the stock data
sp500 = list(reversed(Share('^GSPC').get_historical(start_date, end_date)))
nasdaq = list(reversed(Share('^IXIC').get_historical(start_date, end_date)))

ivv = list(reversed(Share('IVV').get_historical(start_date, end_date)))
qqq = list(reversed(Share('QQQ').get_historical(start_date, end_date)))

sh = list(reversed(Share('SH').get_historical(start_date, end_date)))

# get the dividend data
ivv_dividends = list(reversed(Share('IVV').get_dividend_history(start_date, end_date)))
sh_dividends = list(reversed(Share('SH').get_dividend_history(start_date, end_date)))

# we need to combine the data into a complete lis


# open the file
filename = open(r"C:\py_scripts\pyMarket\MarketData_%s_%s.csv"%(start_date, end_date), 'w')

# add a header
filename.write("Date,Open,Close,Adj_Close,High,Low,Volume\n")
for day in sp500:
  # put the data in the csv file
  string="%s,"%day['Date']
  string+="%s,"%day['Open']
  string+="%s,"%day['Close']
  string+="%s,"%day['Adj_Close']
  string+="%s,"%day['High']
  string+="%s,"%day['Low']
  string+="%s,"%day['Volume']
  string+="\n"

  filename.write(string)

filename.close()
