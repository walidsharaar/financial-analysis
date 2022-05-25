import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt


stock = ["AAPL","XPEV"]
stocks= yf.download(stock, start ="2010-01-01" ,end="2022-26-05" )
data = stocks.loc[:,"close"].copy()



data.plot(figsize=(17,8),fontsize=18)
plt.style.use("seaborn")
plt.show()
