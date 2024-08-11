# Import and name the pandas package
import pandas as pd

# Import the data using a pandas csv reader, turn it into a data frame and name it df_stocks
ts_data = pd.read_csv("/mnt/c/Users/mansh/Downloads/ts_data.csv")
df_stocks = pd.DataFrame(ts_data)

# Convert the format of the first column using to_datetime in pandas and set it as the index column and then print the top 5 rows to see if it worked
df_stocks['DATE'] = pd.to_datetime(df_stocks['DATE'])
df_stocks.set_index('DATE', inplace=True)

print(df_stocks.head())

# Add a new column to the data frame that contains the 7-day simple moving average of the apple stock price and print the top five rows to see that it worked
df_stocks['AAPL_7day_SMA'] = df_stocks['AAPL'].rolling(window=7).mean()
print(df_stocks.head())

df_stocks_TSLA_max = df_stocks['TSLA'].max() # Find the peak Tesla stock price within the period
df_stocks_TSLA_max_date = df_stocks.loc[df_stocks['TSLA'] == df_stocks_TSLA_max].index[0] # Find the date of the peak stock price above
dates = pd.date_range(df_stocks_TSLA_max_date, df_stocks.index[-1]) # Store the date range from peak stock price to end in a variable
dates1 = pd.date_range(df_stocks.index[0], df_stocks_TSLA_max_date) # For testing purposes, store the date range from beginning to peak price date
df_stocks_filtered1 = df_stocks.loc[dates1[0]:dates1[-1]] # Filter the data frame using a date range
df_stocks_filtered = df_stocks.loc[dates[0]:dates[-1]] # Filter the data frame using another date range
df_stocks_TSLA_min = df_stocks_filtered['TSLA'].min() # Find the lowest Tesla stock price after the peak

mdd = ((df_stocks_TSLA_max - df_stocks_TSLA_min) / df_stocks_TSLA_max) * 100 # Calculate the maximum drawdown using the formula provided

print(f"Maximum Drawdown is {mdd}%") # Print the maximum drawdown