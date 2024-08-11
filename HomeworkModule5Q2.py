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

# Store the values of a column ('Market Value') 
val = df_assets['Market Value']
print(val)

df_assets['Total Market Value'] = df_assets['Market Value'] * df_assets['Quantity']

print(df_assets)

highval = df_assets[df_assets['Market Value'] > 1000]
print(highval)

df_assets.loc[df_assets['Asset'] == 'Commodities', 'Market Value'] = 1025

print(df_assets)

sorted_df_assets = df_assets.sort_values(by='Total Market Value', ascending=False)

print(sorted_df_assets)