"""
CP1401 - Checkpoint 2
All Together Now - IT@JCU Coffee
Suggested Solution
See the demonstrations videos for all the details and explanations
"""
import random

MENU_PROMPT = "(O)rder - (D)rink - (R)andom choice - (Q)uit"
VALID_COFFEES = ["Flat White", "Espresso", "Long Black", "Babyccino"]


def main():
    """Coffee ordering program."""
    current_coffee = ""
    print("Welcome to the IT@JCU Coffee Shop")
    print(MENU_PROMPT)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "O":
            current_coffee = get_order()
            print_instructions(current_coffee)
        elif choice == "D":
            if current_coffee == "":
                print("Oh... where's my coffee?")
            else:
                print(f"Mmmm, nice {current_coffee}")
        elif choice == "R":
            # index = random.randint(0, len(VALID_COFFEES) - 1)
            # current_coffee = VALID_COFFEES[index]
            current_coffee = random.choice(VALID_COFFEES)
            print_instructions(current_coffee)
        else:
            print("Invalid option")
        print(MENU_PROMPT)
        choice = input(">>> ").upper()
    print("Thanks for drinking coffee")


def get_order():
    """Get valid coffee order."""
    print("Please choose from: ")
    for coffee in VALID_COFFEES:
        print(coffee, end=" - ")
    coffee_choice = input("? ").title()
    while coffee_choice not in VALID_COFFEES:
        print("Invalid order")
        coffee_choice = input("? ").title()
    return coffee_choice


def print_instructions(current_coffee):
    """Print instructions for current_coffee."""
    print(f"Here's how to make a/n {current_coffee}")
    if current_coffee == "Espresso":
        grind_beans()
        pour_espresso()
    elif current_coffee == "Long Black":
        grind_beans()
        pour_espresso()
        print("- Add hot water to cup")
    elif current_coffee == "Flat White":
        grind_beans()
        pour_espresso()
        steam_milk()
        add_milk()
    elif current_coffee == "Babyccino":
        steam_milk()
        add_milk()
    else:  # Unexpected case
        print("Something went wrong! Unknown coffee.")


def grind_beans():
    """Print instructions for grinding the beans."""
    print("- Insert portafilter into grinder")
    print("- Press grind button to grind beans into portafilter")


def pour_espresso():
    """Print instructions for pouring an espresso."""
    print("- Distribute grounds")
    print("- Tamp grounds")
    print("- Insert full portafilter into group head")
    print("- Press shot button to pour espresso into cup")


def steam_milk():
    """Print instructions for steaming milk."""
    print("- Fill jug with milk")
    print("- Steam milk until nice microfoam formed and milk up to temperature")


def add_milk():
    """Print instructions for adding milk."""
    print("- Swirl milk gently in jug")
    print("- Pour milk into cup... carefully, artistically :)")


main()
