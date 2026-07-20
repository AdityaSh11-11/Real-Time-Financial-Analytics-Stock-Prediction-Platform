"""
charts.py

Reusable Plotly charts for the dashboard.
"""

import plotly.graph_objects as go
import plotly.express as px


# ---------------------------------------------------------
# Candlestick Chart
# ---------------------------------------------------------

def create_candlestick(df, ticker):

    fig = go.Figure()

    fig.add_trace(
        go.Candlestick(
            x=df["Date"],
            open=df["Open"],
            high=df["High"],
            low=df["Low"],
            close=df["Close"],
            name=ticker
        )
    )

    fig.add_trace(
        go.Scatter(
            x=df["Date"],
            y=df["SMA20"],
            mode="lines",
            name="SMA20",
            line=dict(width=2)
        )
    )

    fig.add_trace(
        go.Scatter(
            x=df["Date"],
            y=df["SMA50"],
            mode="lines",
            name="SMA50",
            line=dict(width=2)
        )
    )

    fig.add_trace(
        go.Scatter(
            x=df["Date"],
            y=df["EMA20"],
            mode="lines",
            name="EMA20",
            line=dict(width=2)
        )
    )

    fig.update_layout(
    uirevision="constant"
)

    return fig


# ---------------------------------------------------------
# Volume Chart
# ---------------------------------------------------------

def create_volume_chart(df):

    fig = px.bar(
        df,
        x="Date",
        y="Volume",
        title="Trading Volume"
    )

    fig.update_layout(
        template="plotly_white",
        height=350
    )

    return fig


# ---------------------------------------------------------
# RSI Chart
# ---------------------------------------------------------

def create_rsi_chart(df):

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=df["Date"],
            y=df["RSI14"],
            mode="lines",
            name="RSI"
        )
    )

    fig.add_hline(
        y=70,
        line_dash="dash",
        annotation_text="Overbought"
    )

    fig.add_hline(
        y=30,
        line_dash="dash",
        annotation_text="Oversold"
    )

    fig.update_layout(
        template="plotly_white",
        height=350,
        title="Relative Strength Index"
    )

    return fig


# ---------------------------------------------------------
# MACD Chart
# ---------------------------------------------------------

def create_macd_chart(df):

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=df["Date"],
            y=df["MACD"],
            name="MACD"
        )
    )

    fig.add_trace(
        go.Scatter(
            x=df["Date"],
            y=df["MACD_SIGNAL"],
            name="Signal"
        )
    )

    fig.update_layout(
        template="plotly_white",
        height=350,
        title="MACD"
    )

    return fig


# ---------------------------------------------------------
# Feature Importance
# ---------------------------------------------------------

def create_feature_importance(model, features):

    importance = getattr(model, "feature_importances_", None)

    if importance is None:
        raise ValueError(
        "The supplied model does not expose feature_importances_."
    )

    fig = px.bar(
        x=importance,
        y=features,
        orientation="h",
        labels={
            "x": "Importance",
            "y": "Feature"
        },
        title="Feature Importance"
    )

    fig.update_layout(
        template="plotly_white",
        height=450
    )

    return fig


# ---------------------------------------------------------
# Comparison Chart
# ---------------------------------------------------------

def create_comparison_chart(stock_data):

    """
    stock_data

    {
        "Apple": dataframe,
        "Tesla": dataframe,
        "Microsoft": dataframe
    }
    """

    fig = go.Figure()

    for company, df in stock_data.items():

        normalized = (
            df["Close"] /
            df["Close"].iloc[0]
        ) * 100

        fig.add_trace(

            go.Scatter(

                x=df["Date"],

                y=normalized,

                mode="lines",

                name=company

            )

        )

    fig.update_layout(

        title="Normalized Performance Comparison",

        template="plotly_white",

        height=550,

        yaxis_title="Normalized Price"

    )

    return fig


# ---------------------------------------------------------
# Daily Return Distribution
# ---------------------------------------------------------

def create_return_distribution(df):

    fig = px.histogram(

        df,

        x="Daily_Return",

        nbins=40,

        title="Daily Return Distribution"

    )

    fig.update_layout(

        template="plotly_white",

        height=350

    )

    return fig