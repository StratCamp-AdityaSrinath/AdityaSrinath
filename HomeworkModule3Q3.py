# Creating a game of dice

# Import the necessary modules
import random

dice_roll_1 = [random.randint(1, 6) for i in range(2)] # Generate value from random roll of dice
dice_roll_2 = [random.randint(1, 6) for i in range(2)] # Generate value from random roll of dice

# Sum of dice rolls
score_1 = sum(dice_roll_1)
score_2 = sum(dice_roll_2)

# Empty list to be filled with name of player_1 to catch duplicate names
names_list = []

# Prevent people from breaking code by inputting invalid values
while True: # Ask for name
    try: # Set a condition
        player_1 = str(input("Please enter the name of the first player: "))
    except ValueError: # Provide warning for invalid value
        print("Invalid input. Please enter names only!")
        continue # Go back to first question
    else:
        names_list.append(player_1) # Store the name to prevent duplicate names
        result_1 = score_1 # Not sure why I'm doing this
        break # Prevent an infinite loop

while True: # Ask for name
    try: # Set a condition
        player_2 = str(input("Please enter the name of the second player: "))
        if player_2 in names_list:
            print("Invalid input. No duplicate names!")
            continue # Go back to the first question
    except ValueError: # Provide warning for invalid value
        print("Invalid input. Please enter names only!")
        continue # Go back to first question
    else:
        result_2 = score_2 # Not sure why I'm doing this
        break # Prevent an infinite loop by exiting once the original condition is met

# Print names, scores, and the result of the game
print(f"{player_1}'s score: {result_1}")
print(f"{player_2}'s score: {result_2}")
if result_1 > result_2:
    print(f"{player_1} wins!")
elif result_1 == result_2:
    print("It's a draw!")
else:
    print(f"{player_2} wins!")