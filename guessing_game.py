"""
Data Analysis Techdegree
Project 1 - A Number Guessing Game
--------------------------------
"""

# Import the random and statistics modules.
from random import randint
from statistics import mean, median, multimode
from sys import exit

# Global declarations

guess_totals = []
game_attempts = 0
best_attempt = 0

def show_welcome():
    print("""
-------------------------------------
Welcome to the numbers guessing game!
-------------------------------------
    """)

def get_number():
    return randint(1, 100)

def check_guess(correct_number):
    player_guess = 0
    guess_count = 0

    #   3. Continuously prompt the player for a guess.
    while player_guess != correct_number:
        try:
            player_guess = int(input("I'm thinking of a number between 1 and 100...\t"))

            if player_guess > 100 or player_guess < 1:
                print("That number is invalid. Please try again.")
                continue
            if player_guess > correct_number:
                
                #     a. If the guess is greater than the solution, display to the player "It's lower".
                print("It's lower")
            elif player_guess < correct_number:       

                #     b. If the guess is less than the solution, display to the player "It's higher". 
                print("It's higher")
            else:
            #   4. Once the guess is correct, stop looping, inform the user they "Got it" and store the number of guesses it took in a list.
                print(f"Got it")

            guess_count += 1
        except ValueError:
            print("That number is invalid. Please try again.")
            print("Please enter a whole number between 1 and 100 (inclusive)")
        except Exception as ex:
            print(f"Something went wrong: {ex}")

    return guess_count

def show_scores(guess_count):
    #   5. Display the following data to the player
    #     a. How many attempts it took them to get the correct number in this game
    print(f"Attempt #{game_attempts}")
    print(f"It took you {guess_count} guesses to get the correct number.")
    print(f"Your best attempt was {best_attempt} guesses")
    #     b. The mean of the saved attempts list

def show_stats(guess_count):

    print(f"The average of your guesses is {round(mean(guess_totals))}.")
#     c. The median of the saved attempts list
    print(f"The median of your guesses is {median(guess_totals)}")
#     d. The mode of the saved attempts list
    if len(multimode(guess_totals)) > 1:
        print("There is no mode for your guesses.")
    else:
        print(f"The mode of your guesses is {multimode(guess_totals)}")
    
# Create the start_game function.
def start_game():
# Write your code inside this function.

#   When the program starts, we want to:
#   ------------------------------------
#   1. Display an intro/welcome message to the player.
    show_welcome()
#   2. Store a random number as the answer/solution.
    number_to_guess = get_number()
    return check_guess(number_to_guess)

# Kick off the program by calling the start_game function.
while True:
    game_attempts += 1
    guess_count = start_game()
    guess_totals.append(guess_count)

    if game_attempts == 1:
        best_attempt = guess_count
    elif guess_count < best_attempt:
        best_attempt = guess_count

    show_scores(guess_count)

    #   6. Prompt the player to play again
    #     a. If they decide to play again, start the game loop over.
    #     b. If they decide to quit, show them a goodbye message.
    play_again = input("Y for yes, anything else to exit:\t")
    if play_again.upper() == 'Y':
        continue
    else:
        print("""
-------------------------------------
Final Stats!
-------------------------------------
              """)
        show_stats(guess_count)
        print("Thanks for playing!")
        exit()