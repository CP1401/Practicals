"""
CP1401 - Example program for Practical 6 - Functions
BMI calculation example

Pseudocode

function main()
    height = get_valid_number("Height", 0, 3)
    weight = get_valid_number("Weight", 0, 300)
    bmi = calculate_bmi(height, weight)
    category = determine_weight_category(bmi)
    print bmi, category

function get_valid_number(prompt, low, high)
    print prompt
    get number
    while number < low or number > high
        print error, prompt
        get number
    return number

function calculate_bmi(height, weight)
    return weight / (height ** 2)

function determine_weight_category(bmi)
    if bmi < 18.5
        return underweight
    else if bmi < 25
        return normal
    else if bmi < 30
        return overweight
    else
        return obese
"""


def main():
    # height = float(input("Height (m): "))
    # weight = float(input("Weight (kg): "))
    height = get_valid_number("Height (m): ", 0, 3)
    weight = get_valid_number("Weight (kg): ", 0, 300)
    bmi = calculate_bmi(height, weight)
    category = determine_weight_category(bmi)
    print(f"This BMI is {bmi}, which is considered {category}")


def get_valid_number(prompt, low, high):
    number = float(input(prompt))
    while number < low or number > high:
        print("Invalid input")
        number = float(input(prompt))
    return number


def calculate_bmi(height, weight):
    return weight / (height ** 2)


def determine_weight_category(bmi):
    if bmi < 18.5:
        return "underweight"
    elif bmi < 25:
        return "normal"
    elif bmi < 30:
        return "overweight"
    else:
        return "obese"


def run_tests():
    bmi = calculate_bmi(2, 60)
    print(bmi)  # This should be 15.0
    bmi = calculate_bmi(1.5, 100)
    print(bmi)  # This should be 44.4

    print(determine_weight_category(16))  # This should be underweight
    print(determine_weight_category(25))  # This should be overweight

    height = get_valid_number("Height (m): ", 0, 3)
    print(height)
    weight = get_valid_number("Weight (kg): ", 0, 300)
    print(weight)

# main()
# run_tests()
