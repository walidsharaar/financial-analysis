import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt


stock = ["AAPL","XPEV"]
stocks= yf.download(stock, start ="2020-25-05" ,end="2022-26-05" )
data = stocks.loc[:,"close"].copy()



data.plot(figsize=(17,8),fontsize=18)
plt.style.use("seaborn")
plt.show()

data.head()
#  get value of first row
data.iloc[0]




# check the frequency of google stock as a sample

google = normData.GOOGL.copy().to_frame()
ret= google.pct_change().dropna()

ret.plot(kind="hist",figsize=(12,8),bins=100)
plot.show()

