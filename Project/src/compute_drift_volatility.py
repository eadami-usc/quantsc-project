def compute_monthly_drift_volatility(market_adjusted_returns):
    grouped = market_adjusted_returns.groupby([market_adjusted_returns.index.year, market_adjusted_returns.index.month])
    drift = grouped.mean()
    volatility = grouped.std()
    return drift, volatility