#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 11:40:52 2021

@author: akniels1
"""
from get_all_tickers import get_tickers as gt
import  yfinance as yf
import pandas as pd


finance_tick = gt.get_tickers_filtered(sectors=gt.SectorConstants.FINANCE)
finance_tick = ' '.join(finance_tick)

data = yf.download(finance_tick[0], start="2014-01-01", end="2020-01-01" ,group_by='ticker')
data['ticker'] = finance_tick[0]


class download_data:
    
    
    def Download(): 
    
    
        finance_tick = gt.gt.get_tickers_filtered(sectors=gt.SectorConstants.FINANCE)
        #finance_tick = ' '.join(finance_tick)
        
        tec_tick = gt.get_tickers_filtered(sectors=gt.SectorConstants.TECH)
        #tec_tick = ' '.join(tec_tick)
        
        
        energy_tick = gt.get_tickers_filtered(sectors=gt.SectorConstants.ENERGY)
        #energy_tick = ' '.join(energy_tick)
    
    
    
        data = yf.download(finance_tick[0], start="2014-01-01", end="2020-01-01" ,group_by='Ticker')
        data['ticker'] = finance_tick[0]
        for item in finance_tick[1:]:
            try:
                dat = yf.download(item, start="2014-01-01", end="2020-01-01" ,group_by='ticker')
            except ValueError:
                continue
            dat['ticker'] = item
            if dat.shape[0] == 0:
                continue
            data  = pd.concat([data, dat])
        data.to_csv('Finance.csv') 
    
        tec_data = yf.download(tec_tick[0], start="2014-01-01", end="2020-01-01" ,group_by='Ticker')
        tec_data['ticker'] = tec_tick[0]
        for item in energy_tick[1:]:
            try:
                tdat = yf.download(item, start="2014-01-01", end="2020-01-01" ,group_by='ticker')
            except ValueError:
                continue
            tdat['ticker'] = item
            if tdat.shape[0] == 0:
                continue
            data  = pd.concat([tec_data, tdat])
        tec_data.to_csv('Tech.csv') 
    
        energy_data = yf.download(energy_tick[0], start="2014-01-01", end="2020-01-01" ,group_by='Ticker')
        energy_data['ticker'] = energy_tick[0]
        for item in energy_tick[1:]:
            try:
                edat = yf.download(item, start="2014-01-01", end="2020-01-01" ,group_by='ticker')
            except ValueError:
                continue
            edat['ticker'] = item
            if edat.shape[0] == 0:
                continue
            data  = pd.concat([energy_data, edat])
        energy_data.to_csv('Energy.csv') 

if __name__ == "__main__":
    download_data.Download()



