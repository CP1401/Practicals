"""
CP1401 - Checkpoint 2
Suggested Solutions
Please do not use/view these solutions until you have attempted
the checkpoint challenges yourself!
Use these solutions as a guide to review and improve your completed work.
"""

# Docstrings:
# This is NOT a docstring.
"""This is NOT a docstring."""


def do_something():
    """This IS a docstring."""
    print()
    """This is NOT a docstring"""


def is_valid_password(password):
    """Determine if password is considered valid or not."""
    if len(password) < 6 or " " in password:
        return False
    return True


# 1. Print a line
def question_1():
    """Test question 1."""
    print_line(40)


def print_line(length):
    """Print a line of length hyphens."""
    print("-" * length)


# 2. Is it even?
def is_even(number):
    """Determine if an integer passed into it is even."""
    return number % 2 == 0


def question_2():
    """Test question 2."""
    some_number = int(input("Number: "))
    if is_even(some_number):
        print(f"{some_number} is even")
    else:
        print(f"{some_number} is odd")
    # print(is_even(6))
    # print(is_even(61))


# 3. Get Non-empty String
def get_nonempty_string(prompt):
    """Get non-empty string."""
    string = input(prompt)
    while string == "":
        print("String is too short")
        string = input(prompt)
    return string


def question_3():
    """Get and display a user's details."""
    name = get_nonempty_string("Name: ")
    birthplace = get_nonempty_string("Birthplace: ")
    print(f"your name is {name} and you were born in {birthplace}.")


# 4. Number List
def question_4():
    """Program to make list between minimum and maximum number"""
    minimum = int(input("Minimum number: "))
    maximum = int(input("Maximum number: "))
    while maximum < minimum:
        print(f"Your maximum must be greater than {minimum}")
        maximum = int(input("Maximum number: "))
    # numbers = list(range(minimum, maximum + 1))  # Here's a way you could do this more in fewer lines than below :)
    numbers = []
    for number in range(minimum, maximum + 1):
        numbers.append(number)
    print(numbers)


# 5. Subject List
def question_5():
    """Program to get and process list of subject codes."""
    subjects = []
    subject = input("Enter subject code: ")
    while subject != "":
        if not is_valid_subject(subject):
            print("Invalid subject code")
        else:
            subjects.append(subject.upper())
        subject = input("Enter subject code: ")
    print(f"You do these {len(subjects)} subjects: ")
    subjects.sort()
    for subject in subjects:
        print(subject)
    if "CP1401" in subjects:
        print("You are cool")
    else:
        print("You could be cooler")


def is_valid_subject(subject):
    """Determine if a subject code passed in is valid."""
    if len(subject) != 6:
        return False
    if not subject[:2].isalpha():
        return False
    if not subject[2:].isdigit():
        return False
    return True
