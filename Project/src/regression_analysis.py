import statsmodels.api as sm

def run_regression(y, X, lags=3):
    X_lagged = pd.concat([X.shift(i) for i in range(lags + 1)], axis=1)
    X_lagged.columns = [f'{col}_lag{i}' for i in range(lags + 1) for col in X.columns]
    X_lagged = sm.add_constant(X_lagged.dropna())
    y = y.loc[X_lagged.index]
    model = sm.OLS(y, X_lagged).fit()
    return model