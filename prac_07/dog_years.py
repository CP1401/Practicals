"""CP1401 Practical 7 - Suggested Solution - Dog Years."""


def main():
    """Program to convert human years to dog years from user inputs."""
    age_in_human_years = int(input("Age in human years: "))
    while age_in_human_years >= 0:
        print("Age in dog years is", calculate_dog_years(age_in_human_years))
        age_in_human_years = int(input("Age in human years: "))
    print(":)")


def calculate_dog_years(age_in_human_years):
    """Calculate the age of a dog in dog years based on actual human years."""
    if age_in_human_years <= 2:
        return age_in_human_years * 10.5
    return 21 + (age_in_human_years - 2) * 4


main()
