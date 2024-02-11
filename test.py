import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta
def fetchdata(stock,fromdate,todate,timeframe):
    stock_symbol = stock
    ds=str(fromdate)
    de=str(todate)
    end_date = pd.Timestamp(de)

    start_date = pd.Timestamp(ds)
    intrvl = str(timeframe)

    data = pd.DataFrame(columns=["Date", "Time", "Open", "High", "Low", "Close", "Volume", "Change", "Change Percentage"])

    while start_date <= end_date:
        stock_data = yf.download(stock_symbol, start=start_date, end=start_date + timedelta(days=1), interval=intrvl)
        if not stock_data.empty:
            stock_data.reset_index(inplace=True)
            stock_data["Date"] = stock_data["Datetime"].dt.date
            stock_data["Time"] = stock_data["Datetime"].dt.time
            stock_data["Change"] = stock_data["High"] - stock_data["Low"]
            stock_data["Change Percentage"] = (stock_data["Change"] / stock_data["Open"]) * 100
            data = data._append(stock_data[["Date", "Time", "Open", "High", "Low", "Close", "Volume", "Change", "Change Percentage"]], ignore_index=True)
        start_date += timedelta(days=1)

    data.to_excel("stock_data.xlsx", index=False)
