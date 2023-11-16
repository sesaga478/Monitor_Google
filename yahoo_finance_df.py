import yfinance as yf
import pandas as pd

def yahoo_fin_df(sector,ticker, company, start_date, end_date):
    data = yf.download(ticker, start=start_date, end=end_date)
    df=pd.DataFrame(data['Adj Close'])
    df['sector']=sector
    df['ticker']=ticker
    return df
