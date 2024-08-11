# Import and name the pandas package
import pandas as pd

# Store data in a variable
data = {
    'Asset': ['Bonds','Stocks','Real Estate','Commodities'],
    'Quantity':[120,80,50,70],
    'Market Value':[1200.00,2400.50,3000,950]
}

# Turn data into a dataframe (table) using pandas dataframe function
df_assets = pd.DataFrame(data)

# Store the values of a column ('Market Value') in a variable and print
val = df_assets['Market Value']
print(val)

# Create a new column in the table by multiplying the values of ('Market Value') and ('Quantity') and call it ('Total Market Value') and print the newly-edited data frame
df_assets['Total Market Value'] = df_assets['Market Value'] * df_assets['Quantity']

print(df_assets)

# Filter the data frame for all assets with a market value higher than 1000, store it in a variable, and print
highval = df_assets[df_assets['Market Value'] > 1000]
print(highval)

# Change the market value of commodities and print the newly-edited data frame
df_assets.loc[df_assets['Asset'] == 'Commodities', 'Market Value'] = 1025

print(df_assets)

# Sort the data frame by total market value in descending order (highest value first) and print
sorted_df_assets = df_assets.sort_values(by='Total Market Value', ascending=False)

print(sorted_df_assets)