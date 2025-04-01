import numpy as np
import statsmodels.api as sm

def compute_beta(stock_returns, market_returns):
    X = sm.add_constant(market_returns.dropna())
    model = sm.OLS(stock_returns.dropna(), X).fit()
    return model.params[1]  # beta

def compute_market_adjusted_return(stock_returns, market_returns, beta):
    return stock_returns - beta * market_returns