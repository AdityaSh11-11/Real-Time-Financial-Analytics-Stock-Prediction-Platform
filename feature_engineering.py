"""
feature_engineering.py

Creates technical indicators used by the ML model.
"""

import pandas as pd

from ta.trend import (
    SMAIndicator,
    EMAIndicator,
    MACD
)

from ta.momentum import RSIIndicator

from ta.volatility import BollingerBands


# ---------------------------------------------------------
# Feature Engineering
# ---------------------------------------------------------

def engineer_features(
    df: pd.DataFrame,
    prediction_days: int = 1
):

    df = df.copy()

    # -----------------------------------------------------
    # Moving Averages
    # -----------------------------------------------------

    df["SMA20"] = SMAIndicator(
        close=df["Close"],
        window=20
    ).sma_indicator()

    df["SMA50"] = SMAIndicator(
        close=df["Close"],
        window=50
    ).sma_indicator()

    df["EMA20"] = EMAIndicator(
        close=df["Close"],
        window=20
    ).ema_indicator()

    # -----------------------------------------------------
    # RSI
    # -----------------------------------------------------

    df["RSI14"] = RSIIndicator(
        close=df["Close"],
        window=14
    ).rsi()

    # -----------------------------------------------------
    # MACD
    # -----------------------------------------------------

    macd = MACD(df["Close"])

    df["MACD"] = macd.macd()

    df["MACD_SIGNAL"] = macd.macd_signal()

    # -----------------------------------------------------
    # Bollinger Bands
    # -----------------------------------------------------

    bb = BollingerBands(df["Close"])

    df["BB_UPPER"] = bb.bollinger_hband()

    df["BB_LOWER"] = bb.bollinger_lband()

    # -----------------------------------------------------
    # Daily Return
    # -----------------------------------------------------

    df["Daily_Return"] = df["Close"].pct_change()

    # -----------------------------------------------------
    # Rolling Volatility
    # -----------------------------------------------------

    df["Volatility"] = (
        df["Daily_Return"]
        .rolling(20)
        .std()
    )

    # -----------------------------------------------------
    # Price Distance From SMA20
    # -----------------------------------------------------

    df["Distance_SMA20"] = (
        (df["Close"] - df["SMA20"])
        / df["SMA20"]
    )

    # -----------------------------------------------------
    # Price Distance From EMA20
    # -----------------------------------------------------

    df["Distance_EMA20"] = (
        (df["Close"] - df["EMA20"])
        / df["EMA20"]
    )

    # -----------------------------------------------------
    # Target
    # -----------------------------------------------------

    df["Future_Close"] = df["Close"].shift(
        -prediction_days
    )

    df["Target"] = (
        df["Future_Close"] >
        df["Close"]
    ).astype(int)

    # -----------------------------------------------------
    # Remove Missing Values
    # -----------------------------------------------------

    df.dropna(inplace=True)

    df.reset_index(
        drop=True,
        inplace=True
    )

    return df