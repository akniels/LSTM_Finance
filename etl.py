#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 11:40:52 2021

@author: akniels1
"""
from get_all_tickers import get_tickers as gt
import  yfinance as yf
import pandas as pd


class download_data:
    
    
    def Download(): 
        nasdaq = pd.read_csv('nasdaq_screener.csv')
        # change to list of tickers
        tickers = [i for i in nasdaq['Symbol']]
        # download first row of data
        data = yf.download(tickers[0], start="2014-01-01", end="2021-01-01" ,group_by='Ticker')
        # create row for ticker
        data['ticker'] = tickers[0]
        # for loop to append all other rows to initial one
        for item in tickers[1:]:
            try:
                dat = yf.download(item, start="2014-01-01", end="2021-01-01" ,group_by='ticker')
            except ValueError:
                continue
            dat['ticker'] = item
            if dat.shape[0] == 0:
                continue
            data  = pd.concat([data, dat])
        # write to csv
        data.to_csv('nasdaq.csv') 

if __name__ == "__main__":
    download_data.Download()



