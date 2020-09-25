"""CP1401 Practical 7 - Suggested Solution - Dog Years."""


def main():
    """Calculate dog years for human years inputs."""
    age_in_human_years = int(input("Age in human years: "))
    while age_in_human_years >= 0:
        age_in_dog_years = calculate_dog_years(age_in_human_years)
        print("Age in dog years is", age_in_dog_years)
        age_in_human_years = int(input("Age in human years: "))
    print(":)")


def calculate_dog_years(age_in_human_years):
    """Calculate the age of a dog in 'dog years' based on actual 'human' years."""
    if age_in_human_years <= 2:
        age_in_dog_years = age_in_human_years * 10.5
    else:
        age_in_dog_years = 21 + (age_in_human_years - 2) * 4
    return age_in_dog_years
