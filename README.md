A Machine Learning based web application for predicting the closing price of stocks using historical data. The app utilizes the Random Forest Regressor model to provide real-time predictions based on past stock data, and displays them alongside key technical indicators, such as moving averages and relative strength index (RSI).

Overview:

This project provides a user-friendly interface where users can input a stock ticker (such as AAPL, GOOGL, or MSFT) and get predictions for future stock prices, alongside visualizations like stock trends and technical indicators. The application is built with Streamlit for the frontend, and uses scikit-learn, yfinance, and matplotlib for machine learning, data retrieval, and visualization.

Key Features:

Real-time Stock Predictions: Predict the future closing price of a stock based on historical data.
Interactive User Interface: Streamlit-based web interface for easy interaction and customization.
Visualizations: Includes line plots to visualize the stock price and predicted trends.
Technical Indicators: Uses 50-Day Moving Average (MA50) and Relative Strength Index (RSI) to enhance predictions.

Tech Stack:

Python 3.x: Programming language.
Streamlit: Framework for building interactive data apps.
scikit-learn: Machine learning library for model training and prediction.
yfinance: Library to download historical stock data from Yahoo Finance.
matplotlib: Data visualization library for plotting graphs.
