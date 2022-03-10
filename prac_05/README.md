# Practical 05 - Coding Checkpoint 1

**All students (internal and external), please submit your prac work via LearnJCU each week by the due date.**

_How do you get better at programming?_  
Write more (good) programs!  
And watch/read/study more examples of good programs and programming.  
That's what this checkpoint is all about.

Please note that you already have plenty of practice questions in the first 4 practicals. Do these!  
Solutions for these checkpoint questions are provided as worked solution demonstration videos as well as the final code
here.

Do the numbered questions in a file called `programs.py`

## Input, Processing, Output

**1. Percentage change**

Write a program that calculates a new value based on an original value and a (percentage-like) increase or decrease.  
Ask the user for the original and the change, then print all 3 values (including the new result) in one statement.
Examples (only output is shown):

- Original: 100, Change: 0.05, Result: 105
- Original: 50.5, Change: -0.1, Result: 45.45

## Decision Structures

**2. Time of day**

Make sure you read the note below before completing this question.  
Ask the user for two inputs: the *time of day* (0-23 hours) and if they are *coming* or *going*.  
Then print a statement about their situation, like:

```
It is before noon and you are coming. Hi!  
It is after noon and you are going. Bye!
```

### Note - Don't Repeat Yourself!

Remember the **DRY (Don't Repeat Yourself)** principle?  
The intention with this exercise is for you to see that what the user inputs for these 2 questions are unrelated.  
You can store the results to be printed in string variables and then print a _SINGLE_ output using those variables.  
You do _NOT_ want to handle this with multiple separate print statements; one for each possible outcome.  
Why not?  
Because in _ALL_ cases, you print one thing. So, you should have one single `print` statement... but customise what you
print based on the 2 user inputs.  
Also, there's no such thing as "noon" :) As soon as you hit 12, it's "after noon".  
Do not use any error-checking; just assume the user will enter correct inputs.

**3. Coffee orders**

- Ask the user for white or black coffee
- Ask for their chosen size: small, medium or large
- Then print the cost: For Black: Small = $3, Medium = $4, Large = $5.  
  White coffee costs $1 more no matter what size is chosen, e.g., a white medium is $5.
- If a user makes a mistake with either part of their order, just pick the most expensive option in each case :)  
  E.g., a purple small coffee would cost $4, a black tiny coffee would cost $5, and a green extra small would cost $6.
  (This can be done by thinking about the default case for each user input.)

Once again, please **DRY**. Do you see that white coffee costs $1 more than black? So, you don't need to handle these as
multiple separate cases. You will only need one decision for size, then one decision for colour. Keep it simple!

Note: You can use the string methods `.upper()` or `.lower()` to make your string comparisons case-insensitive, e.g.,

```python
string = input("Prompt: ").lower()
if string == "string":
    print("It matches without capitals")
```

## Repetition Structures

**4. Coffee orders with error-checking**

For this question, duplicate your coffee orders program, and rewrite it as a new version with error-checking.  
You must submit both questions, so don't change the other code.  
Your error-checking should repeat until the user enters valid inputs. Note that this means you no longer assume/choose
the expensive option, because it won't be possible to choose the colour "purple" or a wrong size. Rewrite your code
constructs to take this into consideration effectively if needed.

**5. Accumulation**

Write a program to ask the user for a _low_ value and a _high_ value.  
Then print all the integers between those values inclusive and show the total of those numbers.

Example, if the inputs were `10` and `20`, you would print:

10 11 12 13 14 15 16 17 18 19 20 totals: 165

**Optional:** Add error-checking to ensure that the high value is actually higher than the low value.

## All Together Now

File: `happy_products.py`

Happy Products is an exciting new company that provides happy products to people who use their awesome new software...  
But it's up to you to write this awesome new software.

They want a menu with the options:

- Instructions
- Calculate
- Quit

When you calculate, you are asked how many products you want to buy and at what price (see how exciting this is?).  
If you buy 0-5 items, they're full price, over 5 items and each one is 10% off!  
Examples:

- 5 x $10 products = $50
- 6 x $50 products = $270

Fewer than 0 items is invalid and so are negative/$0 products, so keep prompting the user until they enter valid
inputs.  
The menu should also handle invalid choices by printing "Invalid choice".

The instructions are:
> Enter the number of products you want to buy and your chosen price.
> If you buy 0-5 items, they're full price, over 5 items and each one is 10% off!

## Sample Output

Here is some sample output from a run of the program:

```
Menu:
(I)nstructions
(C)alculate
(Q)uit
Choice: w
Invalid choice
Menu:
(I)nstructions
(C)alculate
(Q)uit
Choice: I
Enter the number of products you want to buy and your chosen price.
If you buy 0-5 items, they're full price, over 5 items and each one is 10% off!
Menu:
(I)nstructions
(C)alculate
(Q)uit
Choice: c
Number of products: -1
Invalid input
Number of products: 0
Price: 450.32
0 x $450.32 products = $0.00
Menu:
(I)nstructions
(C)alculate
(Q)uit
Choice: C
Number of products: 3
Price: 12.34
3 x $12.34 products = $37.02
Menu:
(I)nstructions
(C)alculate
(Q)uit
Choice: c
Number of products: 6
Price: 100
6 x $100.00 products = $540.00
Menu:
(I)nstructions
(C)alculate
(Q)uit
Choice: q
Farewell
```

# Deliverables

This section summarises the expectations for marking in this practical.

Do not zip up your files.  
Please submit each file separately.  
Ensure each file has the correct/exact name.  
Ensure your code is not commented-out.  

- `programs.py` with all of the numbered checkpoint questions:

1. Percentage program (I, P, O)
2. Time of day (Decision)
3. Coffee orders (Decision)
4. Coffee orders with error-checking (Repetition)
5. Accumulation (Repetition)

- `happy_products.py` (All Together Now)
