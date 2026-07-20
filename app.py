"""
===========================================================
Real-Time Financial Data Engineering &
Stock Market Analytics Platform
===========================================================
Author : Your Name
Version : 2.0
===========================================================
"""

from __future__ import annotations

import streamlit as st
import pandas as pd


from config import (
    US_STOCKS,
    INDIA_STOCKS,
    PERIODS,
    PREDICTION_HORIZON,
    FEATURE_COLUMNS
)

from data_pipeline import get_stock_data

from feature_engineering import engineer_features

from model import ModelService

from utils.analysis import (
    detect_trend,
    calculate_risk,
    investment_score,
    generate_recommendation,
    create_summary
)

from utils.company import (
    get_company_info,
    company_metrics
)

from utils.helpers import (
    latest_statistics,
    comparison_row
)

from utils.charts import (
    create_candlestick,
    create_volume_chart,
    create_rsi_chart,
    create_macd_chart,
    create_feature_importance,
    create_comparison_chart,
    create_return_distribution
)

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="Financial Analytics Platform",
    page_icon="📈",
    layout="wide"
)

# =====================================================
# HEADER
# =====================================================

st.markdown("""
<div class="hero">

<h1>Financial Analytics Platform</h1>

<p>
Real-Time Market Intelligence • Machine Learning • Data Engineering
</p>

</div>
""", unsafe_allow_html=True)

st.divider()

# =====================================================
# SIDEBAR
# =====================================================

st.sidebar.title("Dashboard Controls")

market = st.sidebar.radio(

    "Select Market",

    [

        "🇺🇸 United States",

        "🇮🇳 India"

    ]

)

# ---------------------------------------------

if market == "🇺🇸 United States":

    company_name = st.sidebar.selectbox(

        "Company",

        list(US_STOCKS.keys())

    )

    ticker = US_STOCKS[company_name]

else:

    company_name = st.sidebar.selectbox(

        "Company",

        list(INDIA_STOCKS.keys())

    )

    ticker = INDIA_STOCKS[company_name]

# ---------------------------------------------

prediction_label = st.sidebar.selectbox(

    "Prediction Horizon",

    list(PREDICTION_HORIZON.keys())

)

prediction_days = PREDICTION_HORIZON[prediction_label]

# ---------------------------------------------

refresh_data = st.sidebar.checkbox(

    "Refresh Yahoo Finance Data",

    value=False

)

# ---------------------------------------------

if "run_analysis" not in st.session_state:
    st.session_state.run_analysis = False

if st.sidebar.button("Run Analysis"):
    st.session_state.run_analysis = True

# =====================================================
# TABS
# =====================================================

dashboard_tab, prediction_tab, comparison_tab, database_tab, about_tab = st.tabs(

    [

        "Dashboard",

        "Prediction",

        "Compare",

        "Data",

        "About"

    ]

)

# =====================================================
# MAIN PIPELINE
# =====================================================

if st.session_state.run_analysis:

    with st.spinner("Loading Financial Data..."):

        # -------------------------
        # ETL
        # -------------------------

        df = get_stock_data(

            ticker=ticker,

            refresh=refresh_data

        )

        # -------------------------
        # Feature Engineering
        # -------------------------

        df = engineer_features(

            df,

            prediction_days=prediction_days

        )

        latest = df.iloc[-1]

        # -------------------------
        # Company Info
        # -------------------------

        company_info = get_company_info(ticker)

        metrics = company_metrics(company_info)

        stats = latest_statistics(df)

        # -------------------------
        # Model
        # -------------------------

        model = ModelService()

        model.train(df)

        prediction, confidence = model.predict(

            df.tail(1)

        )

        # Ensure model metrics are available for the UI. Try to get from the
        # model object; if not present, attempt evaluate(), otherwise
        # use safe defaults to avoid runtime errors in the dashboard.
        model_metrics = getattr(model, "metrics", None)
        if model_metrics is None:
            try:
                model_metrics = model.train(df)
            except Exception:
                model_metrics = {
                    "accuracy": 0.0,
                    "precision": 0.0,
                    "recall": 0.0,
                    "f1": 0.0,
                    "confusion_matrix": [[0, 0], [0, 0]]
                }

        # -------------------------
        # Business Logic
        # -------------------------

        trend = detect_trend(latest)

        risk, annual_volatility = calculate_risk(df)

        score = investment_score(

            latest,

            prediction,

            confidence,

            annual_volatility

        )

        recommendation, reasons = generate_recommendation(

            latest,

            prediction,

            confidence,

            trend,

            risk

        )

        summary = create_summary(

            latest,

            prediction,

            confidence,

            recommendation,

            trend,

            risk,

            score

        )

        # =====================================================
        # DASHBOARD TAB
        # =====================================================

        with dashboard_tab:

            st.subheader(f"{company_info['Name']}")

            # ---------------------------------------------
            # KPI CARDS
            # ---------------------------------------------

            c1, c2, c3, c4 = st.columns(4)

            c1.metric(
                "Current Price",
                f"{stats['Current Price']:.2f}",
                f"{stats['Daily Return']:.2f}%"
            )

            c2.metric(
                "Recommendation",
                recommendation
            )

            c3.metric(
                "Investment Score",
                f"{score}/100"
            )

            c4.metric(
                "Risk",
                risk
            )

            st.divider()

            # ---------------------------------------------
            # COMPANY INFORMATION
            # ---------------------------------------------

            st.subheader("Company Information")

            left, right = st.columns([1, 2])

            with left:

                st.metric(
                    "Sector",
                    metrics["Sector"]
                )

                st.metric(
                    "Industry",
                    metrics["Industry"]
                )

                st.metric(
                    "Country",
                    metrics["Country"]
                )

                st.metric(
                    "Employees",
                    metrics["Employees"]
                )

            with right:

                st.metric(
                    "Market Cap",
                    metrics["Market Cap"]
                )

                st.metric(
                    "PE Ratio",
                    metrics["PE Ratio"]
                )

                st.metric(
                    "52 Week High",
                    metrics["52 Week High"]
                )

                st.metric(
                    "52 Week Low",
                    metrics["52 Week Low"]
                )

            with st.expander("Business Summary"):

                st.write(
                    company_info["Business Summary"]
                )

            st.divider()

            # ---------------------------------------------
            # AI SUMMARY
            # ---------------------------------------------

            st.subheader("AI Investment Summary")

            st.markdown(summary)

            st.divider()

            # ---------------------------------------------
            # RECOMMENDATION REASONS
            # ---------------------------------------------

            st.subheader("Why this recommendation?")

            for reason in reasons:

                st.success(reason)

            st.divider()

            # ---------------------------------------------
            # CANDLESTICK
            # ---------------------------------------------

            st.subheader("Price Chart")

            st.plotly_chart(

                create_candlestick(

                    df,

                    ticker

                ),

                width="stretch"

            )

            # ---------------------------------------------
            # VOLUME + RSI
            # ---------------------------------------------

            col1, col2 = st.columns(2)

            with col1:

                st.plotly_chart(

                    create_volume_chart(df),

                    width="stretch"

                )

            with col2:

                st.plotly_chart(

                    create_rsi_chart(df),

                    width="stretch"

                )

            # ---------------------------------------------
            # MACD + RETURNS
            # ---------------------------------------------

            col3, col4 = st.columns(2)

            with col3:

                st.plotly_chart(

                    create_macd_chart(df),

                    width="stretch"

                )

            with col4:

                st.plotly_chart(

                    create_return_distribution(df),

                    width="stretch"

                )

            st.divider()

            # ---------------------------------------------
            # FEATURE IMPORTANCE
            # ---------------------------------------------

            st.subheader("Model Feature Importance")

            st.plotly_chart(

                create_feature_importance(

                    model.model,

                    FEATURE_COLUMNS

                ),

                width="stretch"

            )

        # =====================================================
        # PREDICTION TAB
        # =====================================================

        with prediction_tab:

            st.subheader("Machine Learning Prediction")

            direction = (
                "📈 UP"
                if prediction == 1
                else "📉 DOWN"
            )

            confidence_percent = confidence * 100

            # ---------------------------------------
            # Prediction Metrics
            # ---------------------------------------

            p1, p2, p3, p4 = st.columns(4)

            p1.metric(
                "Prediction",
                direction
            )

            p2.metric(
                "Confidence",
                f"{confidence_percent:.2f}%"
            )

            p3.metric(
                "Trend",
                trend
            )

            p4.metric(
                "Risk",
                risk
            )

            st.divider()

            # ---------------------------------------
            # Recommendation Card
            # ---------------------------------------

            if recommendation == "🟢 BUY":
                st.success(f"Recommendation : {recommendation}")

            elif recommendation == "🟡 HOLD":
                st.warning(f"Recommendation : {recommendation}")

            else:
                st.error(f"Recommendation : {recommendation}")

            st.divider()

            # ---------------------------------------
            # Investment Score
            # ---------------------------------------

            st.subheader("Investment Score")

            st.progress(score / 100)

            st.write(f"Score : **{score}/100**")

            st.divider()

            # ---------------------------------------
            # Model Evaluation
            # ---------------------------------------

            st.subheader("Model Evaluation")

            e1, e2 = st.columns(2)

            with e1:

                st.metric(
                    "Accuracy",
                    f"{model_metrics['accuracy']:.2%}"
                )

                st.metric(
                    "Precision",
                    f"{model_metrics['precision']:.2%}"
                )

            with e2:

                st.metric(
                    "Recall",
                    f"{model_metrics['recall']:.2%}"
                )

                st.metric(
                    "F1 Score",
                    f"{model_metrics['f1']:.2%}"
                )

            st.divider()

            # ---------------------------------------
            # Confusion Matrix
            # ---------------------------------------

            st.subheader("Confusion Matrix")

            cm = pd.DataFrame(

                model_metrics["confusion_matrix"],

                index=[
                    "Actual Down",
                    "Actual Up"
                ],

                columns=[
                    "Predicted Down",
                    "Predicted Up"
                ]

            )

            st.dataframe(
                cm,
                use_container_width=True
            )

            st.divider()

            # ---------------------------------------
            # Feature Importance
            # ---------------------------------------

            st.subheader("Top Features")

            st.plotly_chart(
            create_feature_importance(
                model.model,
                FEATURE_COLUMNS
            ),
            use_container_width=True,
            key="dashboard_feature_importance"
            )

            # ---------------------------------------
            # Latest Feature Values
            # ---------------------------------------

            st.subheader("Latest Feature Values")

            latest_features = (
                df.tail(1)[FEATURE_COLUMNS]
                .T
                .reset_index()
            )

            latest_features.columns = [
                "Feature",
                "Value"
            ]

            st.dataframe(
                latest_features,
                width="stretch"
            )

            st.divider()

            # ---------------------------------------
            # Download Prediction
            # ---------------------------------------

            report = pd.DataFrame([
                {
                    "Company": company_name,
                    "Ticker": ticker,
                    "Prediction": direction,
                    "Confidence": round(confidence_percent, 2),
                    "Recommendation": recommendation,
                    "Trend": trend,
                    "Risk": risk,
                    "Investment Score": score
                }
            ])

            st.download_button(
                "Download Prediction Report",
                data=report.to_csv(index=False),
                file_name=f"{ticker}_prediction.csv",
                mime="text/csv"
            )

        # =====================================================
        # COMPARE TAB
        # =====================================================

        with comparison_tab:

            st.subheader("Multi-Company Comparison")

            st.write(
                "Compare up to 3 companies across predictions, "
                "risk, trend, and historical performance."
            )

            # --------------------------------------------
            # Company Selection
            # --------------------------------------------

            if market == "🇺🇸 United States":
                company_options = list(US_STOCKS.keys())
                company_map = US_STOCKS
            else:
                company_options = list(INDIA_STOCKS.keys())
                company_map = INDIA_STOCKS

            selected = st.multiselect(
                "Select Companies",
                options=company_options,
                default=[company_name],
                max_selections=3
            )

            if len(selected) == 0:
                st.info("Please select at least one company.")
            else:

                comparison_results = []

                comparison_chart = {}

                # ----------------------------------------
                # Loop through companies
                # ----------------------------------------

                for company in selected:

                    compare_ticker = company_map[company]

                    compare_df = get_stock_data(
                        compare_ticker,
                        refresh=False
                    )

                    compare_df = engineer_features(
                        compare_df,
                        prediction_days
                    )

                    compare_model = ModelService()

                    compare_model.train(compare_df)

                    compare_prediction, compare_confidence = (
                        compare_model.predict(
                            compare_df.tail(1)
                        )
                    )

                    latest_compare = compare_df.iloc[-1]

                    compare_trend = detect_trend(
                        latest_compare
                    )

                    compare_risk, compare_volatility = (
                        calculate_risk(compare_df)
                    )

                    compare_score = investment_score(
                        latest_compare,
                        compare_prediction,
                        compare_confidence,
                        compare_volatility
                    )

                    compare_recommendation, _ = (
                        generate_recommendation(
                            latest_compare,
                            compare_prediction,
                            compare_confidence,
                            compare_trend,
                            compare_risk
                        )
                    )

                    comparison_results.append(

                        comparison_row(

                            compare_ticker,

                            latest_compare,

                            compare_trend,

                            compare_risk,

                            compare_recommendation,

                            compare_score,

                            compare_confidence

                        )

                    )

                    comparison_chart[company] = compare_df

                # ----------------------------------------
                # Performance Chart
                # ----------------------------------------

                st.subheader("Normalized Performance")

                st.plotly_chart(

                    create_comparison_chart(
                        comparison_chart
                    ),

                    width="stretch"

                )

                st.divider()

                # ----------------------------------------
                # Comparison Table
                # ----------------------------------------

                table = pd.DataFrame(
                    comparison_results
                )

                table = table.sort_values(
                    "Score",
                    ascending=False
                )

                st.subheader("Comparison Summary")

                st.dataframe(
                    table,
                    width="stretch"
                )

                st.divider()

                # ----------------------------------------
                # Best Pick
                # ----------------------------------------

                best = table.iloc[0]

                st.success(
                    f"""
                    Highest Ranked Stock

                    **{best['Ticker']}**

                    Recommendation: {best['Recommendation']}

                    Investment Score: {best['Score']}

                    Confidence: {best['Confidence']}
                    """
                )

                # ----------------------------------------
                # Download
                # ----------------------------------------

                st.download_button(
                    "Download Comparison",
                    table.to_csv(index=False),
                    file_name="comparison.csv",
                    mime="text/csv"
                )

        # =====================================================
        # DATABASE TAB
        # =====================================================

        with database_tab:

            st.subheader("Historical Data")

            st.write(
                "Explore the processed historical stock data."
            )

            st.dataframe(
                df,
                use_container_width=True,
                height=500
            )

            st.download_button(
                label="Download Historical Data",
                data=df.to_csv(index=False),
                file_name=f"{ticker}_historical_data.csv",
                mime="text/csv"
            )

            st.divider()

            st.subheader("Dataset Statistics")

            stats_df = pd.DataFrame({

                "Metric": [

                    "Rows",

                    "Columns",

                    "Start Date",

                    "End Date"

                ],

                "Value": [

                    len(df),

                    len(df.columns),

                    str(df["Date"].min().date()),

                    str(df["Date"].max().date())

                ]

            })

            st.table(stats_df)

            st.divider()

            st.subheader("Latest 20 Records")

            st.dataframe(

                df.tail(20),

                use_container_width=True

            )

        # =====================================================
        # ABOUT TAB
        # =====================================================

        with about_tab:

            st.header("Real-Time Financial Analytics Platform")

            st.markdown("""

### Overview

This project demonstrates a complete end-to-end financial analytics workflow using real-world market data.

---

### Features

- Real-time stock data from Yahoo Finance
- Support for US and Indian stocks
- Automated feature engineering
- Technical indicators (SMA, EMA, RSI, MACD, Bollinger Bands)
- Random Forest prediction model
- Explainable AI recommendations
- Interactive Plotly dashboards
- SQLite database integration
- Multi-company comparison
- CSV export

""")
            

st.markdown("""
<div class="footer">

Built with ❤️ using Streamlit • Plotly • SQLite • Yahoo Finance • Scikit-Learn

</div>
""", unsafe_allow_html=True)