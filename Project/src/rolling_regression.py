import pandas as pd
import statsmodels.api as sm

def rolling_lagged_regression(y, X, window=12, lags=3):
    results = []
    for start in range(0, len(y) - window - lags):
        end = start + window
        y_window = y.iloc[start + lags:end + lags]
        X_lagged = pd.concat([X.iloc[start + lags - i:end + lags - i].reset_index(drop=True) for i in range(lags + 1)], axis=1)
        X_lagged.columns = [f'{col}_lag{i}' for i in range(lags + 1) for col in X.columns]
        X_lagged = sm.add_constant(X_lagged)
        model = sm.OLS(y_window.reset_index(drop=True), X_lagged).fit()
        results.append({
            'start_date': y.index[start + lags],
            'end_date': y.index[end + lags - 1],
            'r_squared': model.rsquared,
            'coefficients': model.params
        })
    return results