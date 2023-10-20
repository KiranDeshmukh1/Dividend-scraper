import yfinance as yf
import pandas as pd
import datetime as dt

def dividentsheet(symbols,startdate,enddate):
    if not isinstance (symbols,list):
        symbols = [symbols]
    
    
    symbol_with_extention = [symbol + ".NS" for symbol in symbols]
    
    
    div = []
    for i in symbol_with_extention:
        inst = yf.Ticker(i)
        inst.history(period='1d',start=startdate,end=enddate)
        div.append(inst.dividends)
    
    df = pd.DataFrame(div,index=symbol_with_extention)
    df.columns = df.columns.month 
    df.fillna(0)
    df = df.groupby(df.columns,axis=1).sum()
    return df
    
    


dividentsheet(["TCS","INFY",'WIPRO'],"2023-01-01","2023-12-30")