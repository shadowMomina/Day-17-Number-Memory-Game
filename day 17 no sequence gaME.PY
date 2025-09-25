"""
Day 17 - Number Memory Game
Author: Momina Raheel
Description:
A simple console-based memory game where the program shows a random number sequence 
for a short time and the player has to type it from memory. Each round the sequence 
gets longer, making it more challenging.
"""

import random   # for generating random numbers
import time     # for adding delay so the user can memorize numbers
import os       # to clear the screen (optional, improves experience)

def clear_screen():
    """Clears the screen for better visibility after showing the number sequence."""
    # Works on Windows, Mac, and Linux
    os.system('cls' if os.name == 'nt' else 'clear')

def generate_sequence(length):
    """Generates a random number sequence of given length as a string."""
    sequence = ''.join(str(random.randint(0, 9)) for _ in range(length))
    return sequence

def play_game():
    """Main function to run the Number Memory Game."""
    print("Welcome to the Number Memory Game!")
    print("You will be shown a number sequence for a few seconds.")
    print("Try to memorize it and then type it correctly.\n")
    score = 0   # keeps track of how many rounds the player survives
    sequence_length = 3  # starting length of the sequence

    while True:
        # Generate and show the sequence
        sequence = generate_sequence(sequence_length)
        print(f"Memorize this number: {sequence}")
        time.sleep(3)  # wait 3 seconds so user can memorize

        clear_screen()  # clear screen to hide the number
        guess = input("Enter the number sequence: ")

        if guess == sequence:
            print("Correct! 🎉")
            score += 1
            sequence_length += 1  # increase difficulty
            print(f"Your score: {score}\n")
            time.sleep(1)
            clear_screen()
        else:
            print("Oops! That was wrong.")
            print(f"The correct sequence was: {sequence}")
            print(f"Your final score: {score}")
            break

if __name__ == "__main__":
    play_game()
