import matplotlib.pyplot as plt

def plot_drift_volatility(drift, volatility, company_name):
    plt.figure()
    drift.plot(title=f"{company_name} – Monthly Drift")
    plt.figure()
    volatility.plot(title=f"{company_name} – Monthly Volatility")

def plot_coefficients_over_time(results, feature_name):
    dates = [r['end_date'] for r in results]
    coefs = [r['coefficients'].get(feature_name, 0) for r in results]
    plt.figure()
    plt.plot(dates, coefs)
    plt.title(f"Rolling Coefficient for {feature_name}")
    plt.xlabel("Date")
    plt.ylabel("Coefficient")