"""
CP1401 Practical 02 - I, P, O - Suggested Solutions

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

# 3. Holiday Cost
HOTEL_COST = 75.0
food_cost = float(input("Daily food cost: $"))
activities_cost = float(input("Daily activities cost: $"))
number_of_days = int(input("Number of days: "))
total = number_of_days * (HOTEL_COST + food_cost + activities_cost)
print("The trip will cost: $", total, sep="")

# 4. i-stop Calculation
# Note: Do not get caught up on fully understanding the "problem domain" and what i-stop is.
# This is just a program to work out a percentage of two time durations.

# i-stop ON:       1m 2s
# Time Stopped:    2m 41s
# Percentage:      38.5%

stop_on_time = int(input("i-stop on in seconds: "))
stopped_time = int(input("Time stopped in seconds: "))
percentage = stop_on_time / stopped_time * 100
i_stop_minutes = stop_on_time // 60
i_stop_seconds = stop_on_time % 60
stopped_minutes = stopped_time // 60
stopped_seconds = stopped_time % 60
print("i-stop ON:      ", i_stop_minutes, "m ", i_stop_seconds, "s", sep="")
print("Time Stopped:   ", stopped_minutes, "m ", stopped_seconds, "s", sep="")
print("Percentage:    ", percentage, "%", sep="")
