"""
CP1401 Practical 03 - Decision Structures - Suggested Solution
"""

# 1. Tax

TAX_RATE_LOW = 0.05  # 5%
TAX_RATE_HIGH = 0.1  # 10%
TAX_THRESHOLD_LOW = 100
TAX_THRESHOLD_HIGH = 1000

print("Python Party Tax Program - Where Tax is a Party")
income = float(input("Income: $"))
if income > TAX_THRESHOLD_HIGH:
    total_tax = income * TAX_RATE_HIGH
elif income >= TAX_THRESHOLD_LOW:
    total_tax = income * TAX_RATE_LOW
else:
    total_tax = 0

take_home_pay = income - total_tax
print("Total tax is: $", total_tax, sep="")
print("Take home pay is: $", take_home_pay, sep="")

# 4. Dog years
# Write a Python program to calculate a dog's age in dog's years.
#
# To do this – Each year of the first two years is equal to 10.5 human years.
# After that, each dog year equals 4 human years.
#
# Expected Output:
# Input a dog's age in human years: 15
# The dog's age in dog's years is 73

# Note: This solution contains "magic numbers".
# It would be good to use CONSTANTS for these, but seems acceptable as it is
# (partly due to how silly this whole dog years thing appears :)

age_in_human_years = int(input("Age in human years: "))
if age_in_human_years <= 2:
    age_in_dog_years = age_in_human_years * 10.5
else:
    age_in_dog_years = 21 + (age_in_human_years - 2) * 4
print("Age in dog years is", age_in_dog_years)
