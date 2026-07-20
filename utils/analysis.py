"""
analysis.py

Business logic for:
- Trend Detection
- Risk Analysis
- Investment Score
- Buy/Hold/Sell Recommendation
"""

import numpy as np


# ----------------------------------------------------
# Trend Detection
# ----------------------------------------------------

def detect_trend(latest):

    sma20 = latest["SMA20"]
    sma50 = latest["SMA50"]

    if sma20 > sma50:
        return "📈 Bullish"

    elif sma20 < sma50:
        return "📉 Bearish"

    return "➡ Sideways"


# ----------------------------------------------------
# Risk Analysis
# ----------------------------------------------------

def calculate_risk(df):

    annual_volatility = (
        df["Daily_Return"].std()
        * np.sqrt(252)
    )

    if annual_volatility < 0.15:
        risk = "🟢 Low"

    elif annual_volatility < 0.30:
        risk = "🟡 Medium"

    else:
        risk = "🔴 High"

    return risk, annual_volatility


# ----------------------------------------------------
# Investment Score
# ----------------------------------------------------

def investment_score(
    latest,
    prediction,
    confidence,
    annual_volatility
):

    score = 0

    # ---------------- Trend ----------------

    if latest["SMA20"] > latest["SMA50"]:
        score += 25

    # ---------------- RSI ----------------

    if 40 <= latest["RSI14"] <= 65:
        score += 20

    elif latest["RSI14"] < 70:
        score += 10

    # ---------------- ML ----------------

    if prediction == 1:
        score += 25

    # ---------------- Confidence ----------------

    score += int(confidence * 20)

    # ---------------- Volatility ----------------

    if annual_volatility < 0.15:
        score += 10

    elif annual_volatility < 0.30:
        score += 5

    return min(score, 100)


# ----------------------------------------------------
# Recommendation Engine
# ----------------------------------------------------

def generate_recommendation(
    latest,
    prediction,
    confidence,
    trend,
    risk
):

    reasons = []

    score = 0

    # Moving Averages

    if latest["Close"] > latest["SMA20"]:
        reasons.append("Price is above SMA20")
        score += 10

    if latest["SMA20"] > latest["SMA50"]:
        reasons.append("SMA20 is above SMA50")
        score += 15

    # RSI

    if latest["RSI14"] < 70:
        reasons.append("RSI indicates healthy momentum")
        score += 15

    else:
        reasons.append("RSI indicates overbought conditions")

    # MACD

    if latest["MACD"] > latest["MACD_SIGNAL"]:
        reasons.append("MACD bullish crossover")
        score += 15

    # Machine Learning

    if prediction == 1:
        reasons.append(
            f"Random Forest predicts upward movement ({confidence:.0%} confidence)"
        )
        score += 25
    else:
        reasons.append(
            f"Random Forest predicts downward movement ({confidence:.0%} confidence)"
        )

    # Volatility

    if risk == "🟢 Low":
        reasons.append("Low historical volatility")
        score += 10

    elif risk == "🟡 Medium":
        reasons.append("Moderate historical volatility")
        score += 5

    else:
        reasons.append("High historical volatility")

    # Final Recommendation

    if score >= 70:
        recommendation = "🟢 BUY"

    elif score >= 45:
        recommendation = "🟡 HOLD"

    else:
        recommendation = "🔴 SELL"

    return recommendation, reasons


# ----------------------------------------------------
# Complete Summary
# ----------------------------------------------------

def create_summary(
    latest,
    prediction,
    confidence,
    recommendation,
    trend,
    risk,
    score
):

    direction = (
        "upward"
        if prediction == 1
        else "downward"
    )

    summary = f"""
### AI Investment Summary

Current Trend : {trend}

Recommendation : {recommendation}

Investment Score : {score}/100

Risk Level : {risk}

The stock is currently showing a **{trend.replace('📈 ','').replace('📉 ','').replace('➡ ','')}** trend.

The machine learning model predicts a **{direction}**
movement with **{confidence:.1%} confidence**.

Current RSI is **{latest['RSI14']:.2f}**.

Current closing price is **{latest['Close']:.2f}**.
"""

    return summary