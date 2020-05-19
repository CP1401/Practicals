"""
CP1401 - Checkpoint 2
Suggested Solutions
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
def print_line(length):
    """Print a line of length hyphens."""
    print("-" * length)

# 2. Is it even?
def is_even(number):
    """Determine if an integer passed into it is even."""
    return number % 2 == 0


# print(is_even(6))
# print(is_even(61))

# 3. Get Non-empty String
# Note that we are using a main function here to test this
def main():
    """Get and display a user's details."""
    name = get_nonempty_string("Name: ")
    birthplace = get_nonempty_string("Birthplace: ")
    print(f"your name is {name} and you were born in {birthplace}.")


def get_nonempty_string(prompt):
    """Get non-empty string."""
    string = input(prompt)
    while string == "":
        print("String is too short")
        string = input(prompt)
    return string


# 4. Write a program that asks the user for a minimum and maximum number,
# then generates a list of integers between those two numbers

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
subjects = []
subject = input("Enter subject code: ")
while subject != "":
    while len(subject) != 6:
        print("Invalid subject code")
        subject = input("Enter subject code: ")
    subjects.append(subject)
    subject = input("Enter subject code: ")
print(f"You do these {len(subjects)} subjects: ")
for subject in subjects:
    print(subject)
if "CP1401" in subjects:
    print("You are cool")
else:
    print("You could be cooler")


# 6. Data Strings
data_strings = ["Result = 95%", "Final Score = 8%", "Relative Value = 178%",
                "Something else that's very important = 9.2%", "x = 42%"]

for string in data_strings:
    start_index = string.find("= ")
    value = float(string[start_index + 2:-1])
    print(value)

# 7. Date Strings

# 8. Subject Code Strings

subject = input("Enter subject code: ")
while subject != "":
    while len(subject) != 6:
        print("Invalid subject code")
        subject = input("Enter subject code: ")
    it_string = ""
    if subject.startswith("CP"):
        it_string = " IT"
    if subject[2] == '1':
        year_string = "first-year"
    elif subject[2] == '2':
        year_string = "second-year"
    elif subject[2] == '3':
        year_string = "third-year"
    else:
        year_string = "Masters or other"
    print(f"That is a {year_string}{it_string} subject.")
    subject = input("Enter subject code: ")
