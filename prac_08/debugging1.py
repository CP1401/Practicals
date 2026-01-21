"""CP1401 - Practical 8 - Debugging."""

# Debug program 1 - friends' names
names = ["Abby", "Jerome", "Olivia", "Monique"]
print("My friends' names: ")

# Fixed: Start the loop at index 0 to include the first name
for i in range(len(names)):
    print(f"{i + 1}. {names[i]}")  # Added 1 to index for correct numbering

# Fixed: Correct the last name index by using len(names) - 1
last_number = len(names) - 1
print(f"The last name (number {last_number + 1}) is {names[last_number]}")  # Display correct index and name

# Debug program 2 - title-casing country names
countries = ("australia", "new zeaLAND", "India")

# Fixed: Convert tuple to a list to modify the country names
countries_list = [country.title() for country in countries]

# Now print the modified country names
print(countries_list)  # country names should be in title-case now
