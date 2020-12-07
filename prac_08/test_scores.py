"""
CP1401 Practical 8 - Lists - Suggested Solution
Test Scores
Write a program that asks the user to enter 5 test scores between 0 and 100.
The program should display a JCU grade for each score and also the average test score.

NOTE: Please remember that solutions are there to help you learn from...
AFTER you have attempted and tried your best.
Do not copy the solutions. Simply copying is not a good way to learn.
"""
NUMBER_OF_SCORES = 4


def main():
    """Test scores program."""
    scores = []
    for i in range(1, NUMBER_OF_SCORES + 1):
        score = float(input(f"Score {i}: "))
        scores.append(score)
    for i in range(NUMBER_OF_SCORES):
        print(f"Score {i + 1} was {scores[i]:5.1f}, which is {determine_grade(scores[i])}")
    average = sum(scores) / len(scores)
    print("The average score was", average)

    # Simpler, no-formatting version:
    # for i in range(NUMBER_OF_SCORES):
    #     score = float(input(f"Score: "))
    #     scores.append(score)
    # for score in scores:
    #     print(f"Score {score}, which is {determine_grade(score)}")
    # average = sum(scores) / len(scores)
    # print("The average score was", average)


def determine_grade(score):
    """Determine a JCU grade based on a score (percentage 0-100)."""
    if score < 50:
        return "N"
    elif score < 65:
        return "P"
    elif score < 75:
        return "C"
    elif score < 85:
        return "D"
    return "HD"


main()
