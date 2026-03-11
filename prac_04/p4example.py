"""
CP1401 Prac - Decision Structures
Example - Birth Month Counter

get birth_month
while birth_month < 1 or birth_month > 12
    display error message
    get birth_month

for count from 1 to birth_month
    display count
"""

birth_month = int(input("Enter your birth month: "))
while birth_month < 1 or birth_month > 12:
    print("Invalid month")
    birth_month = int(input("Enter your birth month: "))

for count in range(1, birth_month + 1):
    print(count, end=" ")
print()
