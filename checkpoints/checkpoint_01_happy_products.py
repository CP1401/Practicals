"""
CP1401 - Coding Checkpoint 1
https://github.com/CP1401/Practicals/blob/master/checkpoints/checkpoint_01.md
Happy Products Suggested Solution

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
MENU = "Menu:\n(I)nstructions\n(C)alculate\n(Q)uit"

print(MENU)
choice = input("Choice: ").lower()
while choice != "q":
    if choice == 'i':
        print("Enter the number of products you want to buy and your chosen price.\nIf you buy 0-5 items, they're full price, over 5 items and each one is 10% off!")
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
        if number_of_products > 5:
            total = total * 0.9
        print("{} x ${:.2f} products = ${:.2f}".format(number_of_products, price, total))
    else:
        print("Invalid choice")
    print(MENU)
    choice = input("Choice: ").lower()
print("Farewell")
