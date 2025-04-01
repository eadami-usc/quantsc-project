from src.fetch_stock_data import fetch_stock_data
from src.capm_adjustment import compute_beta, compute_market_adjusted_return
from src.fetch_patent_data import load_patent_activity
from src.compute_drift_volatility import compute_monthly_drift_volatility
from src.regression_analysis import run_regression

# 1. Load stock & market data
stock = fetch_stock_data("PFE", "2010-01-01", "2022-12-31")
market = fetch_stock_data("^GSPC", "2010-01-01", "2022-12-31")

# 2. Market adjustment via CAPM
beta = compute_beta(stock['log_return'], market['log_return'])
adjusted_returns = compute_market_adjusted_return(stock['log_return'], market['log_return'], beta)

# 3. Compute drift & volatility
monthly_drift, monthly_volatility = compute_monthly_drift_volatility(adjusted_returns.to_frame(name='R'))

# 4. Load patent activity
patents = load_patent_activity("data/patents/pfizer_patent_data.csv")

# 5. Merge and regress
features = patents[['num_patents', 'num_categories', 'num_new_categories']]
drift_model = run_regression(monthly_drift, features)
volatility_model = run_regression(monthly_volatility, features)

# 6. View results
print("Drift Regression Summary:\n", drift_model.summary())
print("Volatility Regression Summary:\n", volatility_model.summary())