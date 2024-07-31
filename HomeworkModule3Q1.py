# When you need to extract characters from a string, always define an empty string
# Prompting user to input text
print("Please Provide a word in English or a name: ")

# Defining the function
def usdefu(text_input):
    vowels = "aeiouAEIOU" # Defining vowels
    text_vowels = "" # Creating an empty string that can be used to store characters later
    text_consonants = "" # Creating an empty string that can be used to store characters later

    # Defining the conditions to identify and print only consonants
    for i in text_input: # Loop through characters in a string
        if i in vowels: # If a character is in the string vowels
            text_vowels += "" # Replace it with an empty string
        else: # Otherwise
            text_consonants += i # Store it

    for i in text_input: # Loop through characters in a string
        if i not in vowels: # If a character is not in the string vowels
            text_consonants += "" # Replace it with an empty string
        else: # Otherwise
            text_vowels += i # Store it
            vowel_count = len(text_vowels) # Count of vowels in the string
    # List of desired output
    final_list = [str(text_input), int(vowel_count), str(text_vowels), str(text_consonants)]
    # Print desired output
    print (final_list)

text_input = input(str()) # Allow user to input content
test = usdefu(text_input) # Run function and call output test