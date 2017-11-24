import pandas_datareader.data as web
from datetime import datetime

df = web.DataReader('TSLA', 'google', datetime(2016, 1, 1))

print(df.head())
print(df.tail())
