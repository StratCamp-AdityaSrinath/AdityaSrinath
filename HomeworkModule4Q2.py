# Import the csv library to help python perform operations on CSV files
import csv
# Import the statistics library to help with statistical operations
import statistics

# Define the function to find the mean price of S&P 500 stocks
def stock_dict(fpname):
    with open(fpname, 'r') as fname: # Open files in read mode and close upon finishing
        content = csv.reader(fname) # Read the csv file and assign all contents to the variable content
        sp500_dict = {rows[0]:rows[1] for rows in content} # Turn the data into a dictionary by creating key-value pairs matching values in the first column with those in the second 
        del sp500_dict[list(sp500_dict.keys())[0]] # Delete the headers
        for k, v in sp500_dict.items(): # Loop over all key-value pairs in the dictionary
            sp500_dict[k] = float(v) # Turn numbers stored as text strings in float values to enable statistical operations
        return round(statistics.mean(sp500_dict.values()),2) # Result of the function should be mean stock price

fpname = "/mnt/c/Users/mansh/Downloads/Homework_Helper_-_Fixed_Coupon_Bond_Pricer/Stock_Info.csv" # Specify file to be input into function
test = stock_dict(fpname) # Assign a variable pass the value of the output of the function applied on the file to it
print(test) # Print the output