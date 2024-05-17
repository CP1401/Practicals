"""
CP1401 Practical 02 - IPO - Suggested Solutions

# Walkthrough Example
get original_price and surcharge_percentage
extra_charge = original_price * surcharge_percentage
total_price = original_price + extra_charge
display total_price

"""

# Example
original_price = float(input("Original price: $"))
surcharge_percentage = float(input("Surcharge % (e.g. 0.15 is 15%): "))
extra_charge = original_price * surcharge_percentage
total_price = original_price + extra_charge
print("The total meal price is $", total_price, sep="")

# # 3. Holiday Cost
HOTEL_COST = 75.0
food_cost = float(input("Daily food cost: $"))
activities_cost = float(input("Daily activities cost: $"))
number_of_days = int(input("Number of days: "))
total = number_of_days * (HOTEL_COST + food_cost + activities_cost)
print("The trip will cost: $", total, sep="")

# 4. - Deep Sleep Calculation
# Total sleep in seconds: 161
# Deep sleep in seconds : 62
# Deep sleep : 1m 2s
# Total sleep: 2m 41s
# Percentage : 38.50931677018634%


total_time = int(input("Total sleep in seconds: "))
deep_time = int(input("Deep sleep in seconds: "))
percentage = deep_time / total_time * 100
total_minutes = total_time // 60
total_seconds = total_time % 60
deep_minutes = deep_time // 60
deep_seconds = deep_time % 60
print("Deep sleep : ", deep_minutes, "m ", deep_seconds, "s", sep="")
print("Total sleep: ", total_minutes, "m ", total_seconds, "s", sep="")
print("Percentage : ", percentage, "%", sep="")
