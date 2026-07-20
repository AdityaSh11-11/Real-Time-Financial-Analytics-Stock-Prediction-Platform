"""
helpers.py

Common utility functions used across the application.
"""

from __future__ import annotations

import pandas as pd


# --------------------------------------------------------
# Latest Stock Statistics
# --------------------------------------------------------

def latest_statistics(df: pd.DataFrame):

    latest = df.iloc[-1]

    previous = df.iloc[-2]

    daily_change = latest["Close"] - previous["Close"]

    daily_return = (daily_change / previous["Close"]) * 100

    stats = {

        "Current Price": round(latest["Close"], 2),

        "Open": round(latest["Open"], 2),

        "High": round(latest["High"], 2),

        "Low": round(latest["Low"], 2),

        "Volume": int(latest["Volume"]),

        "Daily Change": round(daily_change, 2),

        "Daily Return": round(daily_return, 2),

        "52 Week High": round(df["High"].max(), 2),

        "52 Week Low": round(df["Low"].min(), 2),

        "Average Volume": int(df["Volume"].mean())

    }

    return stats


# --------------------------------------------------------
# Format Large Numbers
# --------------------------------------------------------

def human_number(value):

    if isinstance(value, str):
        return value

    if value >= 1_000_000_000:

        return f"{value/1e9:.2f} B"

    if value >= 1_000_000:

        return f"{value/1e6:.2f} M"

    if value >= 1_000:

        return f"{value/1e3:.2f} K"

    return str(value)


# --------------------------------------------------------
# Percentage Formatter
# --------------------------------------------------------

def percent(value):

    return f"{value:.2f}%"


# --------------------------------------------------------
# Currency Formatter
# --------------------------------------------------------

def currency(value):

    return f"${value:,.2f}"


# --------------------------------------------------------
# Prepare Comparison Row
# --------------------------------------------------------

def comparison_row(

    ticker,

    latest,

    trend,

    risk,

    recommendation,

    score,

    confidence

):

    return {

        "Ticker": ticker,

        "Price": round(latest["Close"], 2),

        "RSI": round(latest["RSI14"], 2),

        "Trend": trend,

        "Risk": risk,

        "Score": score,

        "Confidence": f"{confidence:.1%}",

        "Recommendation": recommendation

    }


# --------------------------------------------------------
# Normalize Close Prices
# --------------------------------------------------------

def normalize_prices(df):

    data = df.copy()

    data["Normalized"] = (

        data["Close"]

        / data["Close"].iloc[0]

    ) * 100

    return data