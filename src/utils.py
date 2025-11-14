import pandas as pd
import numpy as np
import yfinance as yf


def get_snp_500_values_per_company(period):
    """
    Fetches the S&P 500 companies' tickers from Wikipedia and calculates their values
    over the given period using yfinance batch download of adjusted close prices.

    Args:
        period (str): The period over which to fetch the stock data (e.g., '1mo', '3mo', '1y').

    Returns:
        dict: A dictionary with company tickers as keys and their values as values.
              If a ticker has insufficient data, its value will be None.
    """
    # 1) Fetch the S&P 500 tickers from Wikipedia (common, reasonably stable source)
    try:
        tables = pd.read_html("https://en.wikipedia.org/wiki/List_of_S%26P_500_companies")
        sp500_table = tables[0]
        tickers = sp500_table['Symbol'].astype(str).tolist()
    except Exception:
        # If the wiki fetch fails, return empty dict rather than crash
        raise RuntimeError("Failed to fetch S&P 500 tickers from Wikipedia.")

    # yfinance expects tickers like BRK-B instead of BRK.B
    tickers = [t.replace('.', '-') for t in tickers]

    # 2) Download adjusted close prices for all tickers at once
    #    Using 'Adj Close' accounts for splits/dividends.
    try:
        adj = yf.download(tickers, period=period, progress=False, threads=True)["Adj Close"]
    except Exception:
        # If batch download fails, fall back to per-ticker download (slower)
        adj = pd.DataFrame({t: yf.download(t, period=period, progress=False)["Adj Close"] for t in tickers})

    # Normalize to DataFrame (if a single ticker, yf returns a Series)
    if isinstance(adj, pd.Series):
        adj = adj.to_frame(name=tickers[0])

    return adj # Return the DataFrame of adjusted close prices


def get_snp_500_values(period):
    """
    Fetches the S&P 500 index values over the given period using yfinance.
    Args:
        period (str): The period over which to fetch the index data (e.g., '1mo', '3mo', '1y').
    Returns:
        pd.Series: A series of adjusted close prices for the S&P 500 index over the specified period.
    """
    return yf.download("^GSPC", period=period, progress=False)['Adj Close']


def simple_returns(prices):
    """
    Calculate simple returns from a series or DataFrame of prices.
    Args:
        prices (pd.Series or pd.DataFrame): Price data.
    Returns:
        pd.Series or pd.DataFrame: Simple returns.
    """
    return prices.pct_change().dropna()


def continuously_compound_returns(prices):
    """
    Calculate compound returns from a series or DataFrame of prices.
    Args:
        prices (pd.Series or pd.DataFrame): Price data.
    Returns:
        pd.Series or pd.DataFrame: Compound returns.
    """
    return prices.apply(lambda x: np.log(x / x.shift(1))).dropna()


def compound_simple_returns_over_period(returns):
    """
    Calculate total compound return over the entire period from a series or DataFrame of simple returns.
    Args:
        returns (pd.Series or pd.DataFrame): Return data.
    Returns:
        pd.Series or pd.DataFrame: Total compound return over the period.
    """
    return (1 + returns).prod() - 1


def compound_continuous_returns_over_period(returns):
    """
    Calculate total compound return over the entire period from a series or DataFrame of continuously compounded returns.
    Args:
        returns (pd.Series or pd.DataFrame): Return data.
    Returns:
        pd.Series or pd.DataFrame: Total compound return over the period.
    """
    return returns.sum()
