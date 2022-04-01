"""
CP1401 Practical 06 - Functions 1 - Suggested Solution
JCU Grades
"""

import random


def main():
    """Display JCU grades from user scores and random ones."""
    score = float(input("Score: "))
    while score >= 0:
        grade = determine_grade(score)
        print(f"The score {score} is {grade}")
        score = float(input("Score: "))

    number_of_scores = int(input("How many random scores: "))
    for i in range(number_of_scores):
        score = random.randint(0, 100)
        grade = determine_grade(score)
        # Notice that the printing of score = is done here, not in the function
        # It is not the function's job (SRP) to know how the grade will be displayed!
        print(f"{score} = {grade}")


def determine_grade(score):
    """Determine JCU grade based on score."""
    if score < 50:
        return "F"
    elif score < 65:
        return "P"
    elif score < 75:
        return "C"
    elif score < 85:
        return "D"
    return "HD"


main()
