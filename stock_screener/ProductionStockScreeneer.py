#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 13:57:17 2017

@author: jeremygould
"""

import os as os
import pandas as pd
import yahoo_finance as yf
import time as time
sp=pd.read_csv('/Users/jeremygould/Documents/Watson_IoT/PMQ/OpenSourceWork/constituents.csv',sep=",", header=0)
#sp.head()
#sp=sp.drop(sp.columns[[1,2]],axis=1)
#sp.head()
#sp.info()
#type(sp)

###converting dataframe column to a list
spTick=sp['Symbol'].tolist()
#sanity check
#type(spTick)
#len(spTick)
nyse=yf.Share('aapl')
print (nyse.get_short_ratio())
###creating a short list to work with
###Set this value to adjust the list length
short1=spTick[0:75]
short2=spTick[75:150]
short3=spTick[150:225]
short4=spTick[225:300]
short5=spTick[300:375]
short6=spTick[375:450]
short7=spTick[450:504]

#print (short6[45:55])
#print (spTick[420:430])
#print (short1[71:75])
#print (short2[0:5])
#print (spTick[70:80])
#print (short)

#small test
stockGroups=(short1, short2,short3,short4,short5,short6,short7)

Ticker=[]
Dividend_yield=[]
Price_book=[]
Price_earnings=[]
Short_ratio=[]
def yahooKeyStats(stock):
        info=yf.Share(stock)
        dy=info.get_dividend_yield()
        try:
            dy=float(dy)
        except TypeError:
            dy='Na'
        pb=info.get_price_book()
        try:
            pb=float(pb)
        except TypeError:
            pb='Na'
        pe=info.get_price_earnings_ratio()
        try:
            pe=float(pe)
        except TypeError:
            pe='Na'
        Dividend_yield.append(dy)
        Price_book.append(pb)
        Price_earnings.append(pe)
        Ticker.append(stock)
        return Dividend_yield, Price_book, Price_earnings, Ticker

def runningFun (stockSet):
    for eachStock in stockSet:
        yahooKeyStats(eachStock)
        time.sleep(1)

def mastercode(allstocks):
    for item in allstocks:
        runningFun(item)
        time.sleep(1)

def screener(stockList):
    stockList.Div_yield[stockList.Div_yield=='Na']=0
    stockList=stockList[stockList.Price_earnings!='Na']
    stockList=stockList.sort('Price_earnings',ascending=True)
    stockList=stockList[stockList.Div_yield>3.00]
    return (stockList)

mastercode(stockGroups)

metrics=pd.DataFrame({'Ticker':Ticker, 'Div_yield':Dividend_yield,'Price_book':Price_book,'Price_earnings':Price_earnings})
#metrics=pd.DataFrame(metrics)

metrics=screener(metrics)
metrics[['Ticker','Div_yield','Price_book','Price_earnings']]
print(metrics)



####
###metrics={'Ticker':Ticker, 'Div_yield':Dividend_yield,'Price_book':Price_book,'Price_earnings':Price_earnings}
####metrics=pd.DataFrame(metrics)
###metrics[['Ticker','Div_yield','Price_book','Price_earnings']]
###print (metrics)


###metrics=screener(metrics)
###metrics=metrics[['Ticker','Div_yield','Price_book','Price_Earnings']]

###THIS IS TEST CODE BUT SHOULD BE THE SHIT!!!###
###WHY ISN'T THIS WORKING???###
###def mastercode(allstocks):
###    for item in allstocks:
###        runningFun(item)
###        time.sleep(30)

###mastercode(stockGroups)

os.chdir('/Users/jeremygould/Documents/Watson IoT/PMQ/OpenSourceWork')
metrics.to_csv('currentStocks.csv',mode='w',index=False)
