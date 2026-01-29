# Constants
NUM_SCORES = 4


def calculate_grade(score):
    """Determine grade based on score."""
    if score >= 85:
        return "HD"  # High Distinction
    elif score >= 65:
        return "C"  # Credit
    elif score >= 50:
        return "P"  # Pass
    else:
        return "F"  # Fail


def get_valid_score(score_number):
    """Prompt the user for a valid score input."""
    score = float(input(f"Score {score_number}: "))
    while score < 0 or score > 100:
        print("Invalid score. Must be between 0 and 100.")
        score = float(input(f"Score {score_number}: "))
    return score


# Main program
def main():
    # Collect scores from user input
    scores = [get_valid_score(i + 1) for i in range(NUM_SCORES)]

    # Calculate average score
    average_score = sum(scores) / NUM_SCORES

    # Determine trend based on the last score
    trend = "positive" if scores[-1] > average_score else "not positive"

    # Display the results
    print("\nGrade results:")
    for i, score in enumerate(scores, 1):
        print(f"Score {i} was {score:.1f}, which is {calculate_grade(score)}")

    print(f"\nThe average score was {average_score:.3f}")
    print(f"The trend is {trend}")


# Run the program
if __name__ == "__main__":
    main()
