# -*- coding: utf-8 -*-
"""
Created on Sat May 14 17:23:46 2016

@author: keith
"""

import datetime

from yahoo_finance import Share


def daterange( start_date, end_date ):
    if start_date <= end_date:
        for n in range( ( end_date - start_date ).days + 1 ):
            yield start_date + datetime.timedelta( n )
    else:
        for n in range( ( start_date - end_date ).days + 1 ):
            yield start_date - datetime.timedelta( n )
 

def hist_to_csv(filename, history,dividends=None):
  # open the file
  outfile = open(filename, 'w')
  
  # add labels
  outfile.write("date,open,close,adj_close,high,low,volume,dividend\n")
  
  for daily_data in history:
      string = "%s,"%daily_data['Date']
      string+="%s,"%daily_data['Open']
      string+="%s,"%daily_data['Close']
      string+="%s,"%daily_data['Adj_Close']
      string+="%s,"%daily_data['High']
      string+="%s,"%daily_data['Low']
      string+="%s,"%daily_data['Volume']
      
      # look through the dividend list for a dividend for this date
      dividend = 0.0
      
      if dividends != None:
          for div in dividends:
              if div['Date'] == daily_data['Date']:
                  dividend = div['Dividends']
              
      string+="%s\n"%dividend
      
      outfile.write(string)
  
  # close the file
  outfile.close()
    
start_date = datetime.date(year=2015, month=1, day = 1)
end_date = datetime.date.today()
print "Processing from %s to %s\n"%(start_date, end_date)

start_string = start_date.strftime("%Y-%m-%d")
end_string = end_date.strftime("%Y-%m-%d")

# get the stock data
path = "C:\\py_scripts\\PyMarket"
sp500 = list(reversed(Share('^GSPC').get_historical(start_string, end_string)))
hist_to_csv("%s\\sp500.csv"%path, sp500)

ivv = list(reversed(Share('IVV').get_historical(start_string, end_string)))
ivv_dividends = list(reversed(Share('IVV').get_dividend_history(start_string, end_string)))
hist_to_csv("%s\\ivv.csv"%path, ivv, ivv_dividends)

sh = list(reversed(Share('SH').get_historical(start_string, end_string)))
sh_dividends = list(reversed(Share('SH').get_dividend_history(start_string, end_string)))
hist_to_csv("%s\\sh.csv"%path, sh, sh_dividends)

"""
nasdaq = list(reversed(Share('^IXIC').get_historical(start_string, end_string)))
qqq = list(reversed(Share('QQQ').get_historical(start_string, end_string)))
qqq_dividends = list(reversed(Share('QQQ').get_dividend_history(start_string, end_string)))
psq = list(reversed(Share('PSQ').get_historical(start_string, end_string)))
psq_dividends = list(reversed(Share('PSQ').get_dividend_history(start_string, end_string)))

# also try QID, SQQQ

# we need to combine the data into a complete lis
for date in daterange(start_date, end_date):
    print date
"""

