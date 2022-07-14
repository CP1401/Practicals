"""
CP1401 - Practical 5 - Coding Checkpoint 1
Happy Products Suggested Solution

Note: some aspects of this solution have been left imperfect on purpose.
Ensure you are using the principles you've learned and applying them carefully.
Do not copy these solutions, but learn from them and consider the principles and patterns.

Enter the number of products you want to buy and your chosen price.
If you buy 0-5 items, they're full price, over 5 items and each one is 10% off!

Pseudocode:
print menu
get choice
while choice != quit
    if choice == 'i'
        print instructions
    else if choice == 'c'
        get number_of_products
        while number_of_products < 0
            print error message
            get number_of_products
        get price
        while price <= 0
            print error message
            get price
        total = number_of_products * price
        if number_of_products > 5
            total = total * 0.9
        print total
    else
        print "Invalid choice"
    print menu
    get choice
print farewell message
"""
DISCOUNT_THRESHOLD = 5
MENU = "Menu:\n(I)nstructions\n(C)alculate\n(Q)uit"

print(MENU)
choice = input("Choice: ").lower()
while choice != "q":
    if choice == 'i':
        print("Enter the number of products you want to buy and your chosen price.")
        print(f"If you buy 0-{DISCOUNT_THRESHOLD} items, they're full price, over {DISCOUNT_THRESHOLD} items and each one is 10% off!")
    elif choice == 'c':
        number_of_products = int(input("Number of products: "))
        while number_of_products < 0:
            print("Invalid input")
            number_of_products = int(input("Number of products: "))
        price = float(input("Price: "))
        while price <= 0:
            print("Invalid input")
            price = float(input("Price: "))
        total = number_of_products * price
        if number_of_products > DISCOUNT_THRESHOLD:
            total = total * 0.9
        print(f"{number_of_products} x ${price:.2f} products = ${total:.2f}")
    else:
        print("Invalid choice")
    print(MENU)
    choice = input("Choice: ").lower()
print("Farewell")
