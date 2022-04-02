#Modules
import numpy as np
import yfinance as yf
import pandas as pd
import pandas_datareader as pdr
import datetime
import time
import requests
import io
#https://aroussi.com/post/python-yahoo-finance
#Documentation for yfinance usability


#Query list of ticker symbols from user
#Initialize list to use with API to pull historical closing prices

ticker_list = []
ticker_1 = str(input("Enter a ticker symbol, or type 'done' if done: "))
ticker_1 = ticker_1.upper()
break_var = ['DONE','STOP']
while ticker_1 not in break_var:
    ticker_list.append(ticker_1)
    ticker_1 = str(input("Enter a ticker symbol, or type 'done' if done: "))
    ticker_1 = ticker_1.upper()

print(ticker_list)
sorted_ticker = ticker_list
ticker_string = ""
newchars = " "

for i in sorted_ticker:
    ticker_string = str(ticker_string + i + newchars)
ticker_string = ticker_string.strip()

data = yf.download(ticker_string,start= "2016-01-01", end = "2021-01-01", interval = "1d", group_by="ticker",threads = True)
for t in range(1,len(sorted_ticker)):
    print(data[t])














# if __name__ == "__main__":
#     ticker_input()



# def ticker_input():

#     ticker_list = []
#     ticker_1 = str(input("Enter a ticker symbol, or type 'done' if done: "))
#     ticker_1 = ticker_1.upper()

#     while ticker_1 != 'DONE' and ticker_1 != 'STOP':
#         ticker_list.append(ticker_1)
#         ticker_1 = str(input("Enter a ticker symbol, or type 'done' if done: "))
#         ticker_1 = ticker_1.upper()

#     sorted_ticker = ticker_list.sort()
#     ticker_string = ""
#     newchars = " "

#     for i in sorted_ticker:
#         ticker_string = (ticker_string + i + newchars)

#     print(ticker_string)

# if __name__ == "__main__":
#     ticker_input()




# data = yf.download(ticker_string,start= "2009-01-01", end = "2019-01-01", group_by="ticker")
# new_average = average(data['TSLA']['Close'])
# print(data)