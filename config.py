"""
Project Configuration
"""

# -----------------------------
# US Stocks
# -----------------------------

US_STOCKS = {
    "Apple": "AAPL",
    "Microsoft": "MSFT",
    "Amazon": "AMZN",
    "Google": "GOOGL",
    "Meta": "META",
    "Tesla": "TSLA",
    "NVIDIA": "NVDA"
}

# -----------------------------
# Indian Stocks
# -----------------------------

INDIA_STOCKS = {
    "Reliance": "RELIANCE.NS",
    "TCS": "TCS.NS",
    "Infosys": "INFY.NS",
    "HDFC Bank": "HDFCBANK.NS",
    "ICICI Bank": "ICICIBANK.NS",
    "State Bank of India": "SBIN.NS",
    "ITC": "ITC.NS",
    "Larsen & Toubro": "LT.NS",
    "Wipro": "WIPRO.NS",
    "Bajaj Finance": "BAJFINANCE.NS"
}

# -----------------------------
# Historical Data
# -----------------------------

PERIODS = [
    "6mo",
    "1y",
    "2y",
    "5y"
]

# -----------------------------
# Prediction Horizon
# -----------------------------

PREDICTION_HORIZON = {
    "1 Day": 1,
    "3 Days": 3,
    "5 Days": 5
}

# -----------------------------
# Machine Learning Features
# -----------------------------

FEATURE_COLUMNS = [
    "SMA20",
    "SMA50",
    "EMA20",
    "RSI14",
    "MACD",
    "MACD_SIGNAL",
    "Daily_Return",
    "Volatility",
    "Distance_SMA20",
    "Distance_EMA20",
]

# -----------------------------
# Dashboard Colors
# -----------------------------

BUY_COLOR = "#2ecc71"
SELL_COLOR = "#e74c3c"
HOLD_COLOR = "#f1c40f"

PRIMARY_COLOR = "#1f77b4"
SECONDARY_COLOR = "#ff7f0e"

# -----------------------------
# Database
# -----------------------------

DATABASE_PATH = "database/stock.db"