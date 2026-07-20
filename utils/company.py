"""
company.py

Fetch company information from Yahoo Finance.
"""

from __future__ import annotations

from typing import Dict, Any

import yfinance as yf


# -----------------------------------------------------
# Company Information
# -----------------------------------------------------

def get_company_info(ticker: str) -> Dict[str, Any]:
    """
    Fetch company metadata from Yahoo Finance.

    Returns a dictionary with safe defaults.
    """

    stock = yf.Ticker(ticker)

    info = stock.info

    return {

        "Name": info.get("longName", ticker),

        "Symbol": ticker,

        "Sector": info.get("sector", "N/A"),

        "Industry": info.get("industry", "N/A"),

        "Country": info.get("country", "N/A"),

        "Employees": info.get(
            "fullTimeEmployees",
            "N/A"
        ),

        "Market Cap": info.get(
            "marketCap",
            "N/A"
        ),

        "Website": info.get(
            "website",
            "N/A"
        ),

        "52 Week High": info.get(
            "fiftyTwoWeekHigh",
            "N/A"
        ),

        "52 Week Low": info.get(
            "fiftyTwoWeekLow",
            "N/A"
        ),

        "Dividend Yield": info.get(
            "dividendYield",
            "N/A"
        ),

        "PE Ratio": info.get(
            "trailingPE",
            "N/A"
        ),

        "Business Summary": info.get(
            "longBusinessSummary",
            "Summary not available."
        )

    }


# -----------------------------------------------------
# Format Market Cap
# -----------------------------------------------------

def format_market_cap(value):

    if value == "N/A":
        return value

    if value >= 1_000_000_000_000:
        return f"${value/1e12:.2f} T"

    if value >= 1_000_000_000:
        return f"${value/1e9:.2f} B"

    if value >= 1_000_000:
        return f"${value/1e6:.2f} M"

    return str(value)


# -----------------------------------------------------
# Company Overview Cards
# -----------------------------------------------------

def company_metrics(info):

    return {

        "Sector": info["Sector"],

        "Industry": info["Industry"],

        "Country": info["Country"],

        "Employees": info["Employees"],

        "Market Cap": format_market_cap(
            info["Market Cap"]
        ),

        "PE Ratio": info["PE Ratio"],

        "52 Week High": info["52 Week High"],

        "52 Week Low": info["52 Week Low"]

    }