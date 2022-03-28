import yfinance as yf
import streamlit as st

st.write("""
# Simple Stock Price App
Shown are the stock **closing price** and ***volume*** of Google!
""")

tickerSymbol = 'GOOGL'
tickerData = yf.Ticker(tickerSymbol)
tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2020-5-31')

tickerSymbol_1 = 'AAPL'
tickerData_1 = yf.Ticker(tickerSymbol_1)
tickerDf_1 = tickerData_1.history(period='1d', start='2010-5-31', end='2020-5-31')

#Data set contains columns: Open	High	Low	Close	Volume	Dividends	Stock Splits

st.write("""
## Closing Price: Google
""")
st.line_chart(tickerDf.Close)

st.write("""
## Closing Price: Apple
""")
st.line_chart(tickerDf_1.Close)

st.write("""
## Volume Price: Google
""")
st.line_chart(tickerDf.Volume)

st.write("""
## Volume Price: Apple
""")
st.line_chart(tickerDf_1.Volume)