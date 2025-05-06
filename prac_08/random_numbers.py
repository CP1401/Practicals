import random

def get_valid_input(prompt, min_value=1, max_value=None):
    """Helper function to get valid input from the user."""
    while True:
        try:
            value = int(input(prompt))
            if value < min_value or (max_value is not None and value > max_value):
                print(f"Please enter a value between {min_value} and {max_value}.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter an integer.")

# Ask user for quantity and maximum value
quantity = get_valid_input("How many random numbers: ", min_value=1)
maximum = get_valid_input("Maximum number: ", min_value=0)

# Generate random numbers
numbers = [random.randint(0, maximum) for _ in range(quantity)]

# Perform operations
print(f"\nThe generated numbers are: {numbers}")
print(f"The minimum is {min(numbers)}")
print(f"The maximum is {max(numbers)}")
print(f"A randomly chosen number is {random.choice(numbers)}")

# Reverse and sort the list
numbers_reversed = numbers[::-1]
numbers_sorted = sorted(numbers)

print(f"The numbers reversed are {numbers_reversed}")
print(f"The numbers sorted are {numbers_sorted}")
