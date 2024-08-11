import pandas as pd

ts_data = pd.read_csv("/mnt/c/Users/mansh/Downloads/ts_data.csv")
df_stocks = pd.DataFrame(ts_data)

df_stocks['DATE'] = pd.to_datetime(df_stocks['DATE'])
df_stocks.set_index('DATE', inplace=True)

#print(df_stocks.head())

#df_stocks['AAPL_7day_SMA'] = df_stocks['AAPL'].rolling(window=7).mean()
#print(df_stocks.head())

df_stocks_TSLA_max = df_stocks['TSLA'].max()
df_stocks_TSLA_max_date = df_stocks.loc[df_stocks['TSLA'] == df_stocks_TSLA_max].index[0]
dates = pd.date_range(df_stocks_TSLA_max_date, df_stocks.index[-1])
dates1 = pd.date_range(df_stocks.index[0], df_stocks_TSLA_max_date)
df_stocks_filtered1 = df_stocks.loc[dates1[0]:dates1[-1]]
df_stocks_filtered = df_stocks.loc[dates[0]:dates[-1]]
df_stocks_TSLA_min = df_stocks_filtered['TSLA'].min()

mdd = ((df_stocks_TSLA_max - df_stocks_TSLA_min) / df_stocks_TSLA_max) * 100

print(f"Maximum Drawdown is {mdd}%")