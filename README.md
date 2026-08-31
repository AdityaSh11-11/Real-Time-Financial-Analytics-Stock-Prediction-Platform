# FinSight: Financial Analytics & Stock Prediction Platform

<div align="center">

![Python](https://img.shields.io/badge/Python-3.12+-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red?style=for-the-badge&logo=streamlit)
![Scikit Learn](https://img.shields.io/badge/Scikit--Learn-Machine%20Learning-orange?style=for-the-badge&logo=scikit-learn)
![SQLite](https://img.shields.io/badge/SQLite-Database-blue?style=for-the-badge&logo=sqlite)
![Plotly](https://img.shields.io/badge/Plotly-Interactive%20Visualization-purple?style=for-the-badge&logo=plotly)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analytics-black?style=for-the-badge&logo=pandas)
![NumPy](https://img.shields.io/badge/NumPy-Scientific%20Computing-blue?style=for-the-badge&logo=numpy)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

</div>

---

## Overview

The **FinSight: Financial Analytics & Stock Prediction Platform** is an end-to-end financial analytics application that combines **Data Engineering, Business Intelligence, Financial Analytics, Machine Learning, and Interactive Data Visualization** into a single enterprise-grade platform.

The platform automatically collects real-time market data from Yahoo Finance, performs feature engineering, computes technical indicators, trains machine learning models, generates stock movement predictions, evaluates investment risk, and presents actionable business insights through an interactive Streamlit dashboard.

Designed using a modular architecture, the application demonstrates the complete analytics lifecycle—from data ingestion and transformation to predictive modeling and executive decision support.

---

## Business Problem

Financial markets generate massive amounts of time-series data every day. Transforming this raw data into meaningful insights requires multiple stages of data processing, feature engineering, predictive modeling, and visualization.

Many retail investors rely on isolated tools that provide either technical indicators, company fundamentals, or machine learning predictions, but rarely integrate all these capabilities into one unified platform.

This project addresses that gap by delivering a complete analytics solution that combines historical analysis, predictive intelligence, risk assessment, and investment recommendations within a single application.

---

## Solution

The platform automates the complete financial analytics workflow by:

- Collecting real-time stock market data from Yahoo Finance.
- Storing historical data in a local SQLite database.
- Performing automated ETL (Extract, Transform, Load) operations.
- Engineering technical indicators and machine learning features.
- Training predictive machine learning models.
- Estimating future stock price direction.
- Measuring investment risk using financial metrics.
- Comparing multiple companies using normalized performance analysis.
- Presenting interactive executive dashboards for business decision-making.

---

## Key Highlights

- End-to-End Financial Analytics Platform
- Automated ETL Pipeline
- Machine Learning-Based Stock Prediction
- Technical Indicator Analysis
- Investment Risk Assessment
- Explainable AI Recommendations
- Executive Business Intelligence Dashboard
- SQLite Data Warehouse
- Interactive Plotly Visualizations
- Supports US & Indian Stock Markets
- Modular Enterprise Architecture
- Downloadable Reports
- Streamlit Interactive Dashboard
- Cached Real-Time Data Pipeline

---

## Project Objectives

- Build an enterprise-grade financial analytics platform.
- Demonstrate practical applications of Data Engineering.
- Apply Machine Learning to financial market prediction.
- Create executive dashboards for investment analysis.
- Automate financial data collection and preprocessing.
- Showcase production-ready Python development practices.
- Provide a scalable architecture for future financial analytics applications.

---

# Financial Analytics Capabilities

The platform provides enterprise-level financial analytics by integrating historical market analysis, technical indicators, predictive analytics, investment intelligence, and business decision support into a unified dashboard.

---

## Market Performance Analytics

Analyze historical market performance using Open, High, Low, Close, and Volume (OHLCV) data.

### Analytics Performed

- Historical Price Analysis
- Daily Return Analysis
- Price Trend Analysis
- Volume Analysis
- Historical Performance Tracking
- 52-Week High & Low Analysis

**Business Value**

Provides investors with a comprehensive understanding of historical stock performance and market behavior.

---

## Technical Analysis

Generate technical indicators commonly used by traders and financial analysts.

### Technical Indicators

- Simple Moving Average (SMA 20)
- Simple Moving Average (SMA 50)
- Exponential Moving Average (EMA 20)
- Relative Strength Index (RSI)
- Moving Average Convergence Divergence (MACD)
- Signal Line
- Daily Percentage Returns

**Business Value**

Helps identify market momentum, trend reversals, overbought conditions, and oversold opportunities.

---

## Predictive Analytics

The platform applies supervised Machine Learning to estimate future stock price direction.

### Machine Learning Workflow

- Feature Engineering
- Historical Data Processing
- Random Forest Classification
- Prediction Confidence Estimation
- Model Performance Evaluation
- Explainable Feature Importance

### Evaluation Metrics

- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix
- Feature Importance Ranking

**Business Value**

Transforms historical market behavior into predictive investment insights.

---

## Risk Analytics

Evaluate investment risk using historical market volatility.

### Risk Metrics

- Annualized Volatility
- Risk Classification
- Trend Detection
- Confidence Analysis

**Business Value**

Supports risk-aware investment decisions by quantifying uncertainty.

---

## Investment Intelligence

The platform combines multiple analytical signals to generate investment recommendations.

### Decision Engine

- Investment Score
- Buy Recommendation
- Hold Recommendation
- Sell Recommendation
- AI Generated Investment Summary
- Recommendation Explanation

**Business Value**

Converts complex financial analytics into actionable investment decisions.

---

## Company Analytics

Retrieve and analyze company fundamentals directly from Yahoo Finance.

### Company Information

- Company Name
- Sector
- Industry
- Country
- Number of Employees
- Market Capitalization
- PE Ratio
- Business Summary

**Business Value**

Combines financial market analysis with business fundamentals for comprehensive investment evaluation.

---

## Comparative Analytics

Compare multiple companies using normalized performance metrics.

### Comparison Features

- Normalized Price Performance
- Prediction Comparison
- Risk Comparison
- Confidence Comparison
- Investment Score Comparison
- Recommendation Comparison

**Business Value**

Supports portfolio selection by enabling side-by-side company evaluation.

---

# Machine Learning Pipeline

```text
Historical Market Data
            │
            ▼
      Data Cleaning
            │
            ▼
   Feature Engineering
            │
            ▼
 Technical Indicators
            │
            ▼
 Feature Selection
            │
            ▼
 Random Forest Model
            │
            ▼
 Prediction Generation
            │
            ▼
 Model Evaluation
            │
            ▼
 Investment Recommendation
```

---

# Data Engineering Pipeline

The platform follows a complete ETL (Extract, Transform, Load) workflow.

```text
Yahoo Finance API
        │
        ▼
Data Extraction
        │
        ▼
Data Validation
        │
        ▼
Data Cleaning
        │
        ▼
Feature Engineering
        │
        ▼
SQLite Database
        │
        ▼
Machine Learning
        │
        ▼
Business Analytics
        │
        ▼
Interactive Dashboard
```

---

# System Architecture

```text
                        Streamlit Dashboard
                               │
        ┌──────────────────────┼──────────────────────┐
        │                      │                      │
        ▼                      ▼                      ▼
 Executive Dashboard     Prediction Engine     Comparison Dashboard
        │                      │                      │
        └──────────────┬───────┴──────────────┬───────┘
                       ▼                      ▼
                Analytics Services     Visualization Layer
                       │
                       ▼
                 Machine Learning Layer
                       │
                       ▼
               Feature Engineering Layer
                       │
                       ▼
                  Data Pipeline (ETL)
                       │
                       ▼
                 SQLite Data Warehouse
                       │
                       ▼
                Yahoo Finance API
```

---

# Project Structure

```text
Real-Time-Financial-Analytics-Platform/

│── app.py

│── config/
│   ├── settings.py
│   ├── constants.py

│── data/
│   ├── data_pipeline.py
│   ├── feature_engineering.py
│   ├── database.py

│── services/
│   ├── analytics_service.py
│   ├── prediction_service.py
│   ├── comparison_service.py

│── models/
│   ├── random_forest.py
│   ├── evaluation.py

│── charts/
│   ├── charts.py

│── dashboard/

│── assets/

│── tests/

│── README.md
│── requirements.txt
```

---

# Technology Stack

| Category | Technologies |
|----------|--------------|
| Programming Language | Python |
| Data Analysis | Pandas, NumPy |
| Machine Learning | Scikit-learn |
| Financial Data | Yahoo Finance API |
| Database | SQLite, SQLAlchemy |
| Dashboard | Streamlit |
| Visualization | Plotly |
| Feature Engineering | Technical Indicators |
| Version Control | Git, GitHub |
| IDE | VS Code |
| Package Management | pip |

---

# Platform Features

## Executive Dashboard

The Executive Dashboard provides a consolidated view of the financial health of a selected company.

### Features

- Real-Time Stock Price Monitoring
- Daily Price Change
- Investment Score
- Buy / Hold / Sell Recommendation
- Company Profile
- Market Capitalization
- PE Ratio
- Industry & Sector Information
- AI Investment Summary
- Interactive Candlestick Chart
- Trading Volume Analysis
- RSI Visualization
- MACD Analysis
- Feature Importance Visualization

---

## Machine Learning Dashboard

Generate AI-powered stock movement predictions.

### Features

- Future Price Direction Prediction
- Prediction Confidence Score
- Model Evaluation Metrics
- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix
- Feature Importance
- Latest Feature Values
- Prediction Report Export

---

## Company Comparison Dashboard

Compare multiple companies simultaneously.

### Features

- Multi-Company Selection
- Performance Comparison
- Investment Score Comparison
- Prediction Comparison
- Confidence Comparison
- Risk Comparison
- Recommendation Comparison
- Download Comparison Report

---

## Historical Database Explorer

Explore processed financial datasets stored locally.

### Features

- Historical Dataset Viewer
- Dataset Statistics
- Recent Records
- CSV Export
- SQLite Data Storage

---

# 📷 Dashboard Preview


---

# Installation

Clone the repository

```bash
git clone https://github.com/yourusername/Enterprise-Financial-Analytics-Platform.git
```

Move into the project directory

```bash
cd Enterprise-Financial-Analytics-Platform
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

# Project Dependencies

Major Python libraries used:

- Streamlit
- Pandas
- NumPy
- Plotly
- Scikit-learn
- SQLAlchemy
- yFinance
- SQLite
- Joblib

---

# Application Workflow

```text
Select Company
        │
        ▼
Download Financial Data
        │
        ▼
Store in SQLite
        │
        ▼
Feature Engineering
        │
        ▼
Machine Learning Prediction
        │
        ▼
Risk Assessment
        │
        ▼
Investment Recommendation
        │
        ▼
Interactive Dashboard
```

---

# Usage

1. Launch the Streamlit application.

2. Select a stock market.

3. Choose a company.

4. Select the prediction horizon.

5. Run the financial analysis.

6. Explore:

- Executive Dashboard
- Prediction Dashboard
- Company Comparison
- Historical Database

7. Export reports as CSV files.

---

# Sample Analytics

The platform automatically computes:

- Daily Return
- Price Trend
- Volume Trend
- SMA
- EMA
- RSI
- MACD
- Prediction Confidence
- Investment Score
- Risk Classification
- Company Fundamentals
- Historical Performance
- Feature Importance

---

# Data Source

Financial market data is collected from:

- Yahoo Finance API

Company metadata includes:

- Market Capitalization
- Industry
- Sector
- Employee Count
- Business Description
- PE Ratio

---

# Machine Learning Model

Current Model

- Random Forest Classifier

Input Features

- OHLCV Data
- SMA20
- SMA50
- EMA20
- RSI14
- MACD
- MACD Signal
- Daily Returns

Output

- Stock Movement Prediction
- Confidence Score
- Feature Importance

---

# Business Value

The platform demonstrates practical implementation of:

- Financial Analytics
- Business Intelligence
- Data Engineering
- Predictive Analytics
- Machine Learning
- Interactive Data Visualization

Suitable for:

- Investment Analysis
- Financial Research
- Educational Demonstrations
- Portfolio Projects
- Analytics Case Studies

---

# Resume Highlights

This project demonstrates experience with:

- End-to-End Data Engineering
- ETL Pipeline Development
- Financial Data Analytics
- Predictive Machine Learning
- Feature Engineering
- Business Intelligence Dashboards
- SQL Database Management
- Interactive Visualization
- Python Development
- Software Architecture
- Streamlit Application Development

---

# Future Enhancements

Planned improvements include:

- XGBoost & LightGBM Models
- LSTM-Based Time Series Forecasting
- Portfolio Optimization
- Sharpe Ratio
- Sortino Ratio
- Maximum Drawdown
- Value at Risk (VaR)
- Correlation Heatmaps
- Sentiment Analysis using Financial News
- Real-Time Market Streaming
- Docker Deployment
- CI/CD with GitHub Actions
- Cloud Deployment on AWS or Azure

---

# Contributing

Contributions are welcome.

1. Fork the repository.
2. Create a new feature branch.
3. Commit your changes.
4. Push to your branch.
5. Open a Pull Request.

---

# License

This project is licensed under the MIT License.

---

# Author

**Aditya Sharma**

Aspiring Data Analyst | Machine Learning Engineer | Data Engineer

### Skills

- Python
- SQL
- Machine Learning
- Financial Analytics
- Data Engineering
- Business Intelligence
- Streamlit
- Plotly
- Scikit-learn
- SQLAlchemy

---

# Support

If you found this project useful:

Star this repository

Fork this repository

Share your feedback

---

> **Enterprise Financial Analytics & AI-Driven Stock Prediction Platform**
>
> *Transforming Financial Data into Actionable Business Intelligence through Data Engineering, Machine Learning, and Interactive Analytics.*
