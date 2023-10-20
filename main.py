import yfinance as yf
import pandas as pd
import datetime as dt

def dividendsheet(symbols,startdate,enddate):
    if not isinstance (symbols,list):
        symbols = [symbols]
    
    
    symbol_with_extention = [symbol + ".NS" for symbol in symbols]
    
    
    div = []
    for i in symbol_with_extention:
        inst = yf.Ticker(i)
        inst.history(period='1d',start=startdate,end=enddate)
        div.append(inst.dividends)
    
    df = pd.DataFrame(div,index=symbol_with_extention)
    df.fillna(0)
    
    df.columns = pd.to_datetime(df.columns)
    
    df.columns = [date.strftime('%B %Y') for date in df.columns]
    
    

    
    
    df = df.groupby(df.columns,axis=1).sum()
    df = df[sorted(df.columns, key=pd.to_datetime)]

    
    return df    
    


### ------- Dividend filter function ----########

def dividend_filter(symbols, startdate, enddate):
    if not isinstance(symbols, list):
        symbols = [symbols]

    symbol_with_extension = [symbol + ".NS" for symbol in symbols]

    div = {}
    for i in symbol_with_extension:
        inst = yf.Ticker(i)
        inst.history(period='1d', start=startdate, end=enddate)
        dividend_data = inst.dividends

        if not dividend_data.empty:
            div[i] = dividend_data

    if div:
        df = pd.concat(div, axis=1)
        df.fillna(0)
        df = df.T

        df.columns = pd.to_datetime(df.columns)
        df.columns = [date.strftime('%B %Y') for date in df.columns]

        df = df.groupby(df.columns, axis=1).sum()
        df = df[sorted(df.columns, key=pd.to_datetime)]
        
    else:
        df = pd.DataFrame()

    return df



