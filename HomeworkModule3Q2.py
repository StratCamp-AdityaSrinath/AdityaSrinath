# Create a bond pricing tool

# Ask python to look in library math and dowload the exponent function for natural logs
from math import exp

# Prevent people from breaking code by inputting invalid values
while True:
    try: # Ask for value
        notional_value = float(input("Please provide a notional (face) value for the bond: "))
    except ValueError: # Provide warning for invalid value
        print("Invalid input. Please enter numbers only!")
        continue # Go back to first question
    else:
        break # Prevent an infinite loop

# Prevent people from breaking code by inputting invalid values
while True:
    try: # Ask for value
        period_size = float(input("Please provide the size of one period in years: "))
    except ValueError: # Provide warning for invalid value
        print("Invalid input. Please enter numbers only!")
        continue # Go back to first question
    else:
        break # Prevent an infinite loop

# Prevent people from breaking code by inputting invalid values
while True: # Ask for value
    try:
        bond_rate = float(input("Please provide the interest / discount rate for each period: "))
    except ValueError: # Provide warning for invalid value
        print("Invalid input. Please enter numbers only!")
        continue # Go back to first question
    else:
        break # Prevent an infinite loop

# Prevent people from breaking code by inputting invalid values
while True: # Ask for value
    try:
        coupon_rate = float(input("Please provide the coupon (as a percentage of the notional (face) value) in decimal form: "))
    except ValueError: # Provide warning for invalid value
        print("Invalid input. Please enter numbers only!")
        continue # Go back to first question
    else:
        break # Prevent an infinite loop

# Prevent people from breaking code by inputting invalid values
while True: # Ask for value
    try:
        bond_term = float(input("Please provide the term of the bond in years: "))
    except ValueError: # Provide warning for invalid value
        print("Invalid input. Please enter numbers only!")
        continue # Go back to first question
    else:
        break # Prevent an infinite loop

# Define bond pricing function using variables listed above that have now had values passed to them by the user
def bond_pricer_function(notional_value, period_size, bond_rate, coupon_rate, bond_term):
    coupon_pv = ((coupon_rate * notional_value) / (exp(bond_rate) - 1)) * (1 - 1 / ((exp(bond_rate))**(bond_term / period_size)))
    nv_pv = notional_value / ((exp(bond_rate))**(bond_term / period_size))
    bond_price = nv_pv + coupon_pv
    rounded_bond_price = round(bond_price, 2) # Round the price to two decimal places
    print(f"${rounded_bond_price}")

# Run function and call output test
test = bond_pricer_function(notional_value, period_size, bond_rate, coupon_rate, bond_term)