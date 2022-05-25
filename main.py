import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt


stock = ["AAPL","XPEV"]
yf.download(stock, start ="2010-01-01" ,end="2022-26-05" )