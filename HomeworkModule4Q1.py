# Define a function to count the number of characters in a text file
def char_counter(fpname):
    try: # For files that exist
        with open(fpname, 'r') as fname: # Open files in read mode and close upon finish
            content = fname.read() # Read contents and store in variable "content"
            char_count = len(content) # Count number of characters
            if char_count > 1: # Set test based on character count
                return True # Return True if the condition is met
            else:
                return False # Return False otherwise
    except FileNotFoundError: # Error handling
        print("File not found!")

while True: # Ask for a filepath
    try: # For valid filepaths
        print("Please insert a filepath") # Print an instruction
        fpname = str(input()) # Allow user to input a response in the form of a filepath
        test = char_counter(fpname) # Submit the user input into the function and call the output "test"
        if test == False: # If the output does not meet the condition of the function
            with open(f"{fpname}", 'w') as shortfile: # Open the file in write mode and close at the end
                shortfile.write("This file is quite possibly empty") # Write the orange text into the file
        else: # If the output does meet the condition of the function
            with open("/mnt/c/Users/mansh/Downloads/Homework_Helper_-_Fixed_Coupon_Bond_Pricer/testtrue.txt", 'w') as truefile: # Create a new file
                truefile.write("This is a new file") # Write the orange text into the file
    except FileNotFoundError: # If the filepath is invalid
        print("File not found!") # Tell the user
        continue # Continue until a valid filepath is submitted
    else:
        break # Prevent an infinite loop