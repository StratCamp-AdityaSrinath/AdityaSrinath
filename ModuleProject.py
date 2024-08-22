# Be sure to get a free APIkey from Alpha Vantage

# Import necessary packages
import os
import numpy as np
import pandas as pd
import statistics as st
import pandas_datareader.data as web
from datetime import datetime
from dateutil.parser import parse

# Starting variables to be used later to set up process
api_key = 'RLWKDC6FM01JVNXK' # This key does not work so don't bother freeloading - go to alpha vantage to get your free key
start_date = datetime(2024,1,2) # Start date as part of effort to limit size of data pull
end_date = datetime(2024,1,31) # End date as part of effort to limit size of data pull
stock_data = {} # Empty dictionary that will be filled with key-value pairs denoting stock tickers-AV data
stock_symbols = [] # Empty list to collect stock tickers input by user
risk_free_rate = ((1.03) ** (1 / 365)) - 1 # Risk-free rate

# Stock Ticker(s)
while True: # Ask for user input (specifically stock tickers)
    try: # If input is valid 
        stock_input = input("Please input the tickers of the stocks you want to analyse: ") # Print an instruction and allow the user to respond with input
        stock_symbols = [ticker.strip().upper() for ticker in stock_input.split(',')] # Format the input and put into the empty stock_symbols list

        if len(stock_symbols) == 0 or (len(stock_symbols) == 1 and stock_symbols[0] == ''): # Call out errors or no input
            raise ValueError("No valid tickers entered.")
        
        break # Prevent an infinite loop
    except ValueError as e: # If input is invalid
        print(f"Invalid input. {e} Please try again!") # Error message
        continue # Ask the user to start again

# Date Range
while True: # Ask for user input (specifically date range)
    try: # If input is valid
        date_input = input("Please input the start and end dates between January 2, 2024, and January 31, 2024 (inclusive) in MM/DD/YYYY format, separated by a hyphen (e.g., 01/02/2024 - 01/05/2024): ") # Print an instruction and allow the user to respond with input
        start_date_input_str, end_date_input_str = date_input.split('-') # Separate the dates in the range
        start_date_input = parse(start_date_input_str.strip()) # Format the start date
        end_date_input = parse(end_date_input_str.strip()) # Format the end date

        if start_date_input < start_date or start_date_input > end_date: # If the start date is outside the range provided in the variables start_date and end_date
            print("Invalid start date! Please follow instructions on date entry.") # Raise an error with a message
            continue # Ask for another date range
        if end_date_input < start_date or end_date_input > end_date: # If the end date is outside the range provided in the variables start_date and end_date
            print("Invalid end date! Please follow instructions on date entry.") # Raise an error with a message
            continue # Ask for another date range
        if end_date_input < start_date_input: # If the end date is before the start date
            print("End date cannot be before start date! Please try again.") # Raise an error with a message
            continue # Ask for another date range
    except (ValueError, TypeError, KeyError, IndexError): # If there is any other kind of invalid input
        print("Invalid entry. Please enter dates in the correct format (MM/DD/YYYY - MM/DD/YYYY)!") # Raise an error with a message
        continue # Ask for another date range
    else: # If everything is kosher
        break # Prevent an infinite loop

# Dictionary containing stock tickers, matched with data from Alpha Vantage
for symbol in stock_symbols: # for each ticker in the list stock_symbols
    try: # If the symbols are valid
        stock_data[symbol] = web.DataReader(symbol,'av-daily',start = start_date_input,end = end_date_input,api_key = api_key) # Pull data from Alpha Vantage for the dates specified by user input and match it to each ticker
    except ValueError as e: # If any of the tickers are invalid (outside US, acquired etc.)
        print(f"Error fetching data for {symbol}: {e}") # Raise an error with a message specifying which ticker is not valid

# From dictionary above to a list of dataframes
df_list = [] # Create an empty list to help turn the dictionary into a dataframe
for symbol, data in stock_data.items(): # Loop through the key-value pairs in the dictionary
    df_stocks = pd.DataFrame(data) # Turn the values into data in the dataframe
    df_stocks['ticker'] = symbol # Turn the keys into headers
    df_list.append(df_stocks) # Add each dataframe for each new key-value pair that is looped through to the initialised list above

# Combine all list items into one dataframe and prepare for analysis
final_df_stocks = pd.concat(df_list, ignore_index=False) # Concatenate the dataframe items in the list into one dataframe
final_df_stocks = final_df_stocks.drop(['open', 'high', 'low', 'volume'], axis=1) # Remove the data columns we don't want (i.e., we only want close)
final_df_stocks = final_df_stocks.reset_index() # reset index to default settings
final_df_stocks = final_df_stocks.rename(columns={'index': 'date'}) # Rename the index column "date"
final_df_stocks = final_df_stocks.pivot(index='date', columns='ticker', values='close') # Pivot the dataframe to make dates the rows and stock tickers the columns

# Price returns for each stock (new columns)
av_daily_returns = final_df_stocks.pct_change().dropna() # Calculate average daily returns and exclude NaN values from operations
av_daily_returns.columns = [col + '_returns' for col in av_daily_returns.columns] # Name each returns column in the format ticker_returns

# Columns arranged for easy viewing
for i, col in enumerate(final_df_stocks.columns): # For all stock ticker columns
    final_df_stocks.insert(i*2 + 1, col + '_returns', av_daily_returns[col + '_returns']) # Place columns with return calculations for each stock immediately to the right of the respective stock price columns

# Portfolio price returns and volatility (new columns)
weights = [1/len(av_daily_returns.columns)] * len(av_daily_returns.columns) # Weight each stock equally (for lack of a stock volume / total investment amount)
av_daily_returns['portfolio_returns'] = av_daily_returns.dot(weights) # Calculate the portfolio returns for the day
av_daily_returns['portfolio_vol'] = av_daily_returns.std(axis=1) # calculate the portfolio volatility for the day
final_df_stocks['portfolio_returns'] = av_daily_returns['portfolio_returns'] # Add portolio returns as a column to the dataframe
final_df_stocks['portfolio_vol'] = av_daily_returns['portfolio_vol'] # Add portfolio volatility as a column to the dataframe

# Daily Sharpe Ratio (new column)
final_df_stocks['daily_sharpe_ratio'] = (final_df_stocks['portfolio_returns'] - risk_free_rate) / final_df_stocks['portfolio_vol'] # Calculate the daily sharpe ratio and name the column daily_sharpe_ratio

# Average price return for each stock (new row)
final_stock_ar_mean = final_df_stocks.mean() # Calculate the means of all columns and store in a variable
final_returns_mean = pd.DataFrame(final_stock_ar_mean).T # Turn the variable into a dataframe that is transposed and now has a single row so that it can be appended to the full dataframe
final_returns_mean.index = ['Mean'] # Provide the soon-to-be-added row with an index named 'Mean'
final_df_stocks = pd.concat([final_df_stocks, final_returns_mean]) # Add the row to the bottom of the full dataframe

# Remove averages where they are not needed
row_to_modify = 'Mean' # Specify the row from which data is to be removed
columns_to_keep = final_df_stocks.filter(regex='_returns').columns # Specify the column(s) where data is to be retained
columns_to_remove = final_df_stocks.columns.drop(columns_to_keep) # Specify that all other columns are to have their data removed
final_df_stocks.loc[row_to_modify, columns_to_remove] = np.nan # For the columns in the specified row, remove content

# Volatility for each stock, as measured by standard deviation of daily price returns from the mean (new row)
final_stock_stdev = final_df_stocks.std() # Calculate the standard deviation of all columns as a measure of volatility and store in a variable
final_returns_stdev = pd.DataFrame(final_stock_stdev).T # Turn the variable into a dataframe that is transposed and now has a single row so that it can be appended to the full dataframe
final_returns_stdev.index = ['StDev'] # Provide the soon-to-be-added row with an index named 'StDev'
final_df_stocks = pd.concat([final_df_stocks, final_returns_stdev]) # Add the row to the bottom of the full dataframe

# Remove standard deviation calculations where they are not needed
row_to_modify = 'StDev' # Specify the row from which data is to be removed
columns_to_keep = final_df_stocks.filter(regex='_returns').columns # Specify the column(s) where data is to be retained
columns_to_remove = final_df_stocks.columns.drop(columns_to_keep) # Specify that all other columns are to have their data removed
final_df_stocks.loc[row_to_modify, columns_to_remove] = np.nan # For the columns in the specified row, remove content

# Portfolio Sharpe Ratio (new row)
portfolio_sharpe_ratio = (final_df_stocks.loc['Mean','portfolio_returns'] - risk_free_rate) / final_df_stocks.loc['StDev','portfolio_returns'] # Calculate the portfolio sharpe ratio using specified datapoints in the full dataframe and store in a variable
portfolio_sharpe_ratio_df = pd.DataFrame([[portfolio_sharpe_ratio]], columns=['portfolio_returns'], index=['PortfolioSR']) # Turn the variable into a dataframe with column name 'portfolio_returns' to help with concatentation and row (index) name PortfolioSR
final_df_stocks = pd.concat([final_df_stocks, portfolio_sharpe_ratio_df]) # Add the new row to the bottom of the full data frame

# Remove Portfolio Sharpe Ratio calculations where they are not needed (wondering if I need this given how it was calculated)
row_to_modify = 'PortfolioSR' # Specify the row from which data is to be removed
columns_to_keep = final_df_stocks.filter(regex='portfolio_returns').columns # Specify the column(s) where data is to be retained
columns_to_remove = final_df_stocks.columns.drop(columns_to_keep) # Specify that all other columns are to have their data removed
final_df_stocks.loc[row_to_modify, columns_to_remove] = np.nan # For the columns in the specified row, remove content

# Export output to csv
final_df_stocks.to_csv("stocks_portfolio.csv")