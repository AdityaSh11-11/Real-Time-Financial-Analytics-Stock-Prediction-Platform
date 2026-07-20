"""
data_pipeline.py

Extract -> Transform -> Load Pipeline
"""

from datetime import datetime

import pandas as pd
import streamlit as st
import yfinance as yf

from database import load_stock_data, save_stock_data


# -------------------------------------------------------
# Download from Yahoo Finance
# -------------------------------------------------------

@st.cache_data(ttl=3600)
def download_stock_data(ticker: str, period: str = "1y") -> pd.DataFrame:
    """
    Download historical stock prices from Yahoo Finance.
    Cache expires after 1 hour.
    """

    df = yf.download(
        ticker,
        period=period,
        auto_adjust=True,
        progress=False
    )

    if df is None or df.empty:
        raise ValueError(f"No data found for {ticker}")

    # Flatten MultiIndex (new yfinance versions)
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)

    df.reset_index(inplace=True)

    return df


# -------------------------------------------------------
# Clean Data
# -------------------------------------------------------

def clean_stock_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean and standardize stock data.
    """

    df = df.copy()

    # Remove duplicate dates
    df.drop_duplicates(subset=["Date"], inplace=True)

    # Sort oldest -> newest
    df.sort_values("Date", inplace=True)

    # Reset index
    df.reset_index(drop=True, inplace=True)

    # Ensure numeric columns
    numeric_cols = [
        "Open",
        "High",
        "Low",
        "Close",
        "Volume"
    ]

    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    # Remove missing values
    df.dropna(inplace=True)

    return df


# -------------------------------------------------------
# Save Pipeline
# -------------------------------------------------------

def refresh_database(ticker: str, period: str = "1y") -> pd.DataFrame:
    """
    Download latest data and store in SQLite.
    """

    df = download_stock_data(
        ticker=ticker,
        period=period
    )

    df = clean_stock_data(df)

    save_stock_data(df, ticker)

    return df


# -------------------------------------------------------
# Read Pipeline
# -------------------------------------------------------

def get_stock_data(
    ticker: str,
    period: str = "1y",
    refresh: bool = False
) -> pd.DataFrame:
    """
    Main entry point for the application.

    If refresh=True:
        Download fresh data.

    Else:
        Load from database.
        If database empty -> download.
    """

    if refresh:
        return refresh_database(ticker, period)

    database_df = load_stock_data(ticker)

    if database_df.empty or refresh:
        return refresh_database(ticker, period)

    # Rename DB columns back to app format
    database_df = database_df.rename(
        columns={
            "date": "Date",
            "open": "Open",
            "high": "High",
            "low": "Low",
            "close": "Close",
            "volume": "Volume"
        }
    )

    database_df["Date"] = pd.to_datetime(database_df["Date"])

    return database_df


# -------------------------------------------------------
# Latest Price
# -------------------------------------------------------

def latest_price(df: pd.DataFrame) -> float:
    """
    Returns latest closing price.
    """

    return float(df.iloc[-1]["Close"])


# -------------------------------------------------------
# Price Change
# -------------------------------------------------------

def daily_change(df: pd.DataFrame):

    last = df.iloc[-1]["Close"]

    previous = df.iloc[-2]["Close"]

    change = last - previous

    percent = (change / previous) * 100

    return change, percent


# -------------------------------------------------------
# Dataset Summary
# -------------------------------------------------------

def dataset_summary(df):

    return {

        "Rows": len(df),

        "Start Date": df["Date"].min(),

        "End Date": df["Date"].max(),

        "Highest": round(df["High"].max(), 2),

        "Lowest": round(df["Low"].min(), 2),

        "Average Volume": int(df["Volume"].mean())

    }