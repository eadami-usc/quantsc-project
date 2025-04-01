import yfinance as yf
import pandas as pd

def fetch_stock_data(ticker, start_date, end_date):
    data = yf.download(ticker, start=start_date, end=end_date)
    data['log_return'] = (data['Adj Close'] / data['Adj Close'].shift(1)).apply(lambda x: np.log(x))
    return data[['Adj Close', 'log_return']]