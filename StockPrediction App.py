import streamlit as st
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor

# ===================== User Input ===================== #
st.title("Stock Price Prediction")

# Sidebar input for stock ticker and date range
st.sidebar.header("User Input")
ticker = st.sidebar.text_input("Enter Stock Ticker", "AAPL")  # Default to AAPL
start_date = st.sidebar.date_input("Start Date", pd.to_datetime("2023-01-01"))
end_date = st.sidebar.date_input("End Date", pd.to_datetime("2025-01-01"))

# ===================== Fetch Stock Data ===================== #
stock_data = yf.download(ticker, start=start_date, end=end_date)

#Handle Empty Data (If no data found, show error)
if stock_data.empty:
    st.error(f"No data found for {ticker} in the selected date range. Try a different range.")
    st.stop()  # Stop further execution

# ===================== Feature Engineering ===================== #
# Calculate Moving Average (MA50) and Relative Strength Index (RSI)
stock_data['MA50'] = stock_data['Close'].rolling(window=50).mean()
stock_data['RSI'] = 100 - (100 / (1 + stock_data['Close'].diff().rolling(window=14).mean()))

#Remove rows with missing values
stock_data.dropna(inplace=True)

#Ensure enough data for training
if len(stock_data) < 50:
    st.error("Not enough data for meaningful prediction. Try a larger date range.")
    st.stop()

# Prepare features for prediction
features = stock_data[['MA50', 'RSI']]

# ===================== Model ===================== #
# Train the model (RandomForestRegressor)
model = RandomForestRegressor(n_estimators=100)
model.fit(features[:-1], stock_data['Close'][:-1])  # Use all but the last data point for training

# Make prediction for the last day in the dataset
predicted_price = model.predict(features.tail(1))

# ===================== Display Results ===================== #
st.subheader(f"Predicted Closing Price for {ticker} on {end_date}: ${predicted_price[0]:.2f}")

# ===================== Visualization ===================== #
st.subheader(f"Stock Price Trend for {ticker}")

fig, ax = plt.subplots(figsize=(10, 5))

# Plot actual closing price
ax.plot(stock_data.index, stock_data['Close'], label="Actual Closing Price", color='blue')

# Plot the 50-day moving average
ax.plot(stock_data.index, stock_data['MA50'], label="50-Day Moving Average", linestyle="dashed", color='orange')

# Mark the predicted closing price with a red dot
ax.scatter(stock_data.index[-1], predicted_price, color='red', label="Predicted Price", marker="o", s=100)

# Add labels and title
ax.legend()
ax.set_xlabel("Date")
ax.set_ylabel("Price ($)")
ax.set_title(f"{ticker} Stock Price Prediction")

# Display the plot in Streamlit
st.pyplot(fig)




