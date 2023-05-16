import yfinance as yf
import matplotlib.pyplot as plt
from datetime import datetime

ticker = str(input('Give me your ticker: '))
start = str(input('Give me the countdown start time: '))
end = str(input('Give me the countdown end time: '))

if not end:
    end = datetime.now()
data = yf.download(ticker,start,end)
data['Adj Close'].plot()
plt.show()
