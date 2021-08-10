# an application to get stock prices and graph them
"""
To run this application copy launch terminal and enter:
streamlit run streamlit_app.py

If it fails to launch, make sure your terminal is pointing at the folder
containing this file.

"""

import streamlit as st
import datetime as dt
import pandas_datareader as pdr

today = dt.date.today()
start_date = today - dt.timedelta(days = 365)

def user_inputs():
    st.sidebar.header("User Inputs")
    ticker = st.sidebar.text_input('Ticker', 'AAPL')
    start = st.sidebar.date_input("Start", start_date)
    end = st.sidebar.date_input("End", today)
    button = st.sidebar.button('Get chart')
    return ticker, start, end, button

def get_data(ticker, start, end):
    data = pdr.get_data_yahoo(ticker, start, end)["Close"]
    return data

def main():

    ticker, start, end, button = user_inputs()

    if button:
        data = get_data(ticker, start, end)
        st.title(f"Closing prices for {ticker}")
        st.line_chart(data)

if __name__ == "__main__":
    main()