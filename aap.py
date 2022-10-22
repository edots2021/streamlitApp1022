import yfinance as yf #야후에서 증권정보 가져오는 모듈
import streamlit as st
import datetime
import plotly.graph_objects as go

st.write("# 주식차트")

#ticker = "TSLA"
ticker = st.text_input("ticker 입력>>")

data = yf.Ticker(ticker)
today = datetime.datetime.today().strftime("%Y-%m-%d") # Y는 대문자이어야 함
df = data.history(period="1d",start="2015-01-01",end=today) #하루치 데이터를 가져 와라
st.dataframe(df)

st.write("## 종가기준")
st.line_chart(df["Close"])
st.bar_chart(df["Volume"])

candle = go.Candlestick(x=df.index, open=df["Open"], close=df["Close"],high=df["High"], low=df["Low"])
layout = go.Layout(yaxis={"fixedrange":False})
fig = go.Figure(data=[candle],layout=layout)
st.plotly_chart(fig)
