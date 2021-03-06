import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt


stock = ["GOOGL","AMZN","TSLA"]
stocks= yf.download(stock, start ="2020-25-05" ,end="2022-26-05" )
data = stocks.loc[:,"Close"].copy()


#plot the data

data.plot(figsize=(17,8),fontsize=18)
plt.style.use("seaborn")
plt.show()


data.head()
#  get value of first row
data.iloc[0]

# percentage of change
data.pct_change()

# remove the null values
com = data.pct_change().dropna()
com.describe()

#mean and std

sum= com.describe().T.loc[:,["mean","std"]]
sum


# Stock Risk Analysis

sum.plot.scatter(x="std",y="mean",figsiz=(12,8), s=50, fontsize=15)
for i in sum.index:
    plt.annotate(i,xy=(sum.loc[i,"std"]+0.002,sum.loc[i,"mean"]+0.002),size=15)

#

# check the frequency of google stock as a sample
google = normData.GOOGL.copy().to_frame()
ret= google.pct_change().dropna()

ret.plot(kind="hist",figsize=(12,8),bins=100)
plot.show()
