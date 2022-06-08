"""
CP1401 - menu-driven program using functions - Guessing Game.

Things to note:
- Main contains the main things including the whole menu (never use a 'menu' function)
- Each menu choice is a section of the program implemented using a function
- Parameters are passed as needed:
    - play(low, high) - the play function needs to know both low and high, so these are passed in
    - set_limit(low) - this function only needs low
- Values are returned as needed:
    - play returns nothing because it doesn't need to
    - set_limit returns the new high (notice main uses this returned value and stores it in high)
- See how the number_of_games variable is NOT passed to play (or any function)?
  play does not need to know the number_of_games; that's NOT its job
  main updates number_of_games; this IS its job
  We _could_ pass number_of_games into play and have it update it, but that would be poor...
  Why?  - think of each function's job... SRP!
        - play is a function to play a single game; it should not know how many other games have been played
        - by not passing this, we simplify the play function (two parameters instead of three)
        - we could copy the play function to another program that just played once and never used number_of_games

Pseudocode:
Things to note:
- Functions (calls and headers) in pseudocode look almost identical to Python
- You MUST specify the parameters and returns

DEFAULT_LOW = 1
DEFAULT_HIGH = 10

function main()
    low = DEFAULT_LOW
    high = DEFAULT_HIGH
    number_of_games = 0
    get choice
    while choice != "Q"
        if choice == "P"
            play(low, high)
            number_of_games += 1
        else if choice == "S"
            high = set_limit(low)
        else
            print error message
        get choice
    print ending message, number_of_games

function play(low, high)
    secret = random number between low and high
    number_of_guesses = 1
    get guess
    while guess != secret
        number_of_guesses += 1
        if guess < secret
            print Higher
        else
            print Lower
        get guess
    print success message, number_of_guesses

function set_limit(low)
    get new_high
    while new_high <= low
        get new_high
    return new_high
"""

import random

DEFAULT_LOW = 1
DEFAULT_HIGH = 10


def main():
    """Menu-driven guessing game with option to change high limit."""
    low = DEFAULT_LOW
    high = DEFAULT_HIGH
    number_of_games = 0
    print("Welcome to the guessing game")
    choice = input("(P)lay, (S)et limit, (Q)uit: ").upper()
    while choice != "Q":
        if choice == "P":
            play(low, high)
            number_of_games += 1
        elif choice == "S":
            high = set_limit(low)
        else:
            print("Invalid choice")
        choice = input("(P)lay, (S)et limit, (Q)uit: ").upper()
    print(f"Thanks for playing ({number_of_games} times)!")


def play(low, high):
    """Play guessing game using current low and high values."""
    secret = random.randint(low, high)
    number_of_guesses = 1
    guess = int(input(f"Guess a number between {low} and {high}: "))
    while guess != secret:
        number_of_guesses += 1
        if guess < secret:
            print("Higher")
        else:
            print("Lower")
        guess = int(input(f"Guess a number between {low} and {high}: "))
    print(f"You got it in {number_of_guesses} guesses!")


def set_limit(low):
    """Set high limit to new value from user input."""
    print("Set new limit")
    new_high = int(input(f"Enter a new high value, above {low}: "))
    while new_high <= low:
        new_high = int(input(f"Enter a new high value, above {low}: "))
    return new_high


main()
