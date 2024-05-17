"""
CP1401 Practical 04 - Repetition Structures - Suggested Solution
Please remember to use these solutions responsibly
- to enhance your learning, not to avoid learning.
If you get stuck on something, go back to the teaching and work hard to solve the problem.
"""

# 3. Write a program that prints smiley and frowny faces until the user quits.
# The user should see a menu like this: (S)miley (F)rowny (Q)uit
# Make the program print a smiley face (if they press 's'),
# a frowny face, or an error message ("Invalid choice") depending on their choice.
# When the user quits, print "Farewell".

print("(S)miley (F)rowny (Q)uit")
choice = input("> ").upper()
while choice != "Q":
    if choice == "S":
        print(":)")
    elif choice == "F":
        print(":(")
    else:
        print("Invalid choice")
    print("(S)miley (F)rowny (Q)uit")
    choice = input("> ").upper()
print("Farewell")

# 4. Accumulation
# Average Age
total_age = 0
number_of_people = 0
age = int(input("Age: "))
while age >= 0:
    total_age += age
    number_of_people += 1
    age = int(input("Age: "))
if number_of_people != 0:
    average = total_age / number_of_people
    print(average)
else:
    print("No valid average")

# 6. Nested Loops
# Write a program that asks the user for a number of rows and columns, then prints the numbers to mach, like:
# Rows: 3
# Columns: 7
# 0 1 2 3 4 5 6
# 0 1 2 3 4 5 6
# 0 1 2 3 4 5 6

number_of_rows = int(input("Rows: "))
number_of_columns = int(input("Columns: "))
for i in range(number_of_rows):
    for j in range(number_of_columns):
        print(j, end=" ")
    print()
