This project predicts the closing price of a given stock (e.g., AAPL) based on historical stock data. The app uses Random Forest Regressor and allows users to input stock tickers, specify a date range, and get predictions along with a graphical representation of stock trends.

Features
Stock Prediction: Predict the closing price for a given stock.
Visualization: Plot stock price data and the predicted closing price.
User Input: Specify the stock ticker and the date range via a user-friendly sidebar.
Stock Indicators: Incorporates features like 50-day moving average (MA50) and Relative Strength Index (RSI) for the prediction model.
Tech Stack
Python: Programming language used.
Streamlit: Framework for building interactive apps.
yfinance: Fetch historical stock data.
Scikit-learn: For the Random Forest Regressor model.
Matplotlib: For data visualization.
Getting Started
Prerequisites
Make sure you have the following installed:

Python 3.x (preferably Python 3.7 or higher)
pip for managing Python packages
Installation
Clone this repository to your local machine:
bash
Copy
Edit
git clone https://github.com/your-username/stock-price-prediction.git
cd stock-price-prediction
Install the required dependencies:
bash
Copy
Edit
pip install -r requirements.txt
This will install:

streamlit
yfinance
scikit-learn
matplotlib
pandas
Running the App
To start the app, run the following command:

bash
Copy
Edit
streamlit run app.py
This will launch the Streamlit app in your web browser, where you can input stock tickers (e.g., AAPL, GOOGL, NVDA) and date ranges to see the predictions and trends.

Usage
Open the app in your browser.
In the sidebar:
Enter the stock ticker (e.g., AAPL, GOOGL, NVDA).
Select Start Date and End Date.
View the predicted stock price along with the graph displaying the stock's actual closing prices and moving averages.
Example
Ticker: AAPL (Apple Inc.)
Start Date: January 1, 2023
End Date: January 1, 2025
The app will display:

Predicted closing price for the selected date.
A graph showing the actual stock prices, the 50-day moving average, and the predicted closing price.
Future Enhancements
Sentiment Analysis: Integrate sentiment analysis based on news articles to improve prediction accuracy.
Model Tuning: Experiment with other machine learning models and hyperparameters.
Additional Features: Incorporate other technical indicators (e.g., Bollinger Bands, MACD) to enhance the prediction model.
