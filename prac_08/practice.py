# Practice file for extending random_numbers.py
import random


def generate_random_numbers(quantity, maximum):
    """
    Generates a list of random numbers within the specified range.

    Parameters:
    quantity (int): The number of random numbers to generate.
    maximum (int): The maximum value a random number can take.

    Returns:
    list: A list of random numbers.
    """
    return [random.randint(0, maximum) for _ in range(quantity)]


def calculate_properties(numbers, maximum):
    """
    Calculates various properties of the given list of numbers.

    Parameters:
    numbers (list): A list of numbers.
    maximum (int): The maximum value used in generating random numbers.

    Returns:
    dict: A dictionary containing the total, average, numbers above half of maximum, squares, and halved values.
    """
    total = sum(numbers)
    average = total / len(numbers) if numbers else 0
    half_max = maximum / 2
    over_half = [num for num in numbers if num > half_max]
    squares = [num ** 2 for num in numbers]
    halved = [num / 2 for num in numbers]

    return {
        "total": total,
        "average": average,
        "over_half": over_half,
        "squares": squares,
        "halved": halved,
        "half_max": half_max
    }


def display_results(numbers, properties):
    """
    Displays the results of the calculations.

    Parameters:
    numbers (list): The list of random numbers.
    properties (dict): The dictionary containing the calculated properties.
    """
    print(f"The numbers are: {numbers}")
    print(f"Total: {properties['total']}")
    print(f"Average: {properties['average']:.2f}")
    print(f"Numbers over half of maximum ({properties['half_max']}): {properties['over_half']}")
    print(f"Squares: {properties['squares']}")
    print(f"Halved: {properties['halved']}")


# Main program flow
if __name__ == "__main__":
    quantity = 5
    maximum = 50

    # Generate random numbers
    numbers = generate_random_numbers(quantity, maximum)

    # Calculate the properties of the numbers
    properties = calculate_properties(numbers, maximum)

    # Display the results
    display_results(numbers, properties)
