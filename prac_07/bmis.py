"""CP1401 Practical 7 - Suggested Solution - BMIs."""


def main():
    """Various BMIs (Body Mass Index)"""
    for height in range(150, 200, 10):
        height /= 100
        for weight in range(50, 101, 10):
            bmi = calculate_bmi(height, weight)
            category = determine_weight_category(bmi)
            print(f"Height {height}m, Weight {weight:3}kg = BMI {bmi:.1f}, considered {category}")
    # Fixed-height version:
    # height = 1.75
    # for weight in range(50, 101, 2):
    #     bmi = calculate_bmi(height, weight)
    #     category = determine_weight_category(bmi)
    #     print(f"Height {height}m, Weight {weight}kg = BMI {bmi:.1f}, considered {category}")


def calculate_bmi(height, weight):
    """Calculate Body Mass Index based on height and weight."""
    return weight / (height ** 2)


def determine_weight_category(bmi):
    """Determine the weight group (category) in adults 20 years old or older based on BMI."""
    if bmi < 18.5:
        return "underweight"
    elif bmi < 25:
        return "normal"
    elif bmi < 30:
        return "overweight"
    else:
        return "obese"


main()
