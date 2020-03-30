# Coding Checkpoint 1 

**This is not an assessed practical, but a collection of practice exercises for self-evaluation.**  
You do not need to submit anything for this work.  

Please note that you already have plenty of practice questions in the first 4 practicals. Do these!  
Solutions for these checkpoint questions are provided as worked solution demonstration videos in your LearnJCU site (or live lecture/recording).

## Input, Processing, Output

1. Write a program that calculates a new value based on an original value and a (percentage-like) increase or decrease.  
Example:

- Original: 100, Change: 0.05, Result: 105
- Original: 50.5, Change: -0.1, Result: 45.45

## Decision Structures

2. Ask the user for the time of day (0-23 hours) and if they are *coming* or *going*.  
Then print a statement about their situation like:  
> It is before noon and you are coming. Hi!  
> It is after noon and you are going. Bye!

3. Coffee orders made simple.  

- Ask the user for white or black coffee  
- Ask for their chosen size: small, medium or large
- Then print the cost: For Black, Small = $3, Medium = $4, Large = $5. White coffee costs $1 more per size.  
- If a user makes a mistake with their order, just pick the more expensive option :)  
Note: You can use the string methods `.upper()` or `.lower()` to make your string comparisons case insensitive, e.g.  

```python
string = input("Prompt: ").lower()
if string == "string":
    print("It matches without capitals")
```

## Repetition Structures
4. Add error-checking to the coffee order program so you repeat until you get valid inputs.

5. Write a program to ask the user for a low value and a high value, then print all of the integers between those values inclusive and show the total of those numbers.  
Example, if the inputs were `10` and `20`, you would print:  

    10 11 12 13 14 15 16 17 18 19 20 totals: 165 

## All Together Now

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

Under 0 items is invalid and so are negative/$0 products, so keep prompting the user until they enter valid inputs.  
The menu should also handle invalid choices by printing "Invalid choice". 

The instructions are:
> Enter the number of products you want to buy and your chosen price.
> If you buy 0-5 items, they're full price, over 5 items and each one is 10% off!

