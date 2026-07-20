"""
database.py

Handles all database operations for the Stock Market Analytics Platform.
"""

import os
import pandas as pd

from sqlalchemy import create_engine, text

from config import DATABASE_PATH

# ---------------------------------------------------
# Create Database Engine
# ---------------------------------------------------

os.makedirs("database", exist_ok=True)

engine = create_engine(
    f"sqlite:///{DATABASE_PATH}",
    echo=False
)


# ---------------------------------------------------
# Initialize Database
# ---------------------------------------------------

def initialize_database():
    """
    Create stock_data table if it does not exist.
    """

    query = """
    CREATE TABLE IF NOT EXISTS stock_data (

        ticker TEXT,
        date TEXT,

        open REAL,
        high REAL,
        low REAL,
        close REAL,

        volume REAL,

        PRIMARY KEY (ticker, date)

    );
    """

    with engine.begin() as conn:
        conn.execute(text(query))


# ---------------------------------------------------
# Save Data
# ---------------------------------------------------

def save_stock_data(df, ticker):
    """
    Save stock data into SQLite.

    Duplicate dates are ignored.
    """

    initialize_database()

    database_df = df.copy()

    database_df["ticker"] = ticker

    database_df = database_df.rename(
        columns={
            "Date": "date",
            "Open": "open",
            "High": "high",
            "Low": "low",
            "Close": "close",
            "Volume": "volume"
        }
    )

    required = [
        "ticker",
        "date",
        "open",
        "high",
        "low",
        "close",
        "volume"
    ]

    database_df = database_df[required]

    with engine.begin() as conn:

        for _, row in database_df.iterrows():

            conn.execute(
                text(
                    """
                    INSERT OR REPLACE INTO stock_data
                    (
                        ticker,
                        date,
                        open,
                        high,
                        low,
                        close,
                        volume
                    )

                    VALUES
                    (
                        :ticker,
                        :date,
                        :open,
                        :high,
                        :low,
                        :close,
                        :volume
                    )
                    """
                ),
                {
                    "ticker": row["ticker"],
                    "date": str(row["date"]),
                    "open": float(row["open"]),
                    "high": float(row["high"]),
                    "low": float(row["low"]),
                    "close": float(row["close"]),
                    "volume": float(row["volume"])
                }
            )


# ---------------------------------------------------
# Load Data
# ---------------------------------------------------

def load_stock_data(ticker):
    """
    Load a ticker from SQLite.
    """

    initialize_database()

    query = text(
        """
        SELECT *

        FROM stock_data

        WHERE ticker=:ticker

        ORDER BY date
        """
    )

    return pd.read_sql(
        query,
        engine,
        params={"ticker": ticker}
    )


# ---------------------------------------------------
# Available Stocks
# ---------------------------------------------------

def available_tickers():
    """
    Return all stored tickers.
    """

    query = text(
        """
        SELECT DISTINCT ticker

        FROM stock_data
        """
    )

    return pd.read_sql(
        query,
        engine
    )


# ---------------------------------------------------
# Delete Stock
# ---------------------------------------------------

def delete_stock(ticker):

    query = text(
        """
        DELETE

        FROM stock_data

        WHERE ticker=:ticker
        """
    )

    with engine.begin() as conn:

        conn.execute(
            query,
            {"ticker": ticker}
        )


# ---------------------------------------------------
# Database Statistics
# ---------------------------------------------------

def database_summary():

    total_rows = pd.read_sql(

        "SELECT COUNT(*) AS rows FROM stock_data",

        engine

    )

    total_tickers = pd.read_sql(

        "SELECT COUNT(DISTINCT ticker) AS tickers FROM stock_data",

        engine

    )

    return {

        "rows": int(total_rows.iloc[0]["rows"]),

        "tickers": int(total_tickers.iloc[0]["tickers"])

    }