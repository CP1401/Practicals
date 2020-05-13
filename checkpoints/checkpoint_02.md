# Coding Checkpoint 2

**This checkpoint IS an assessed practical, but is also a collection of practice exercises for self-evaluation based on things you should know by now (nothing new).**  
You DO need to submit your (own) work, even though solutions are provided.  

Solutions for these checkpoint questions are provided as worked solution demonstration videos in your LearnJCU site (or live lecture/recording).

### Use Docstrings
Please watch the checkpoint 2 video lecture on docstrings before starting this work.  

For each of your functions, write a brief function **docstring**.  
Here's a good example for a function that checks to see if a password is valid:

```python
def is_valid_password(password):
    """Determine if password is considered valid or not."""
    if len(password) < 6 or " " in password:
        return False
    return True
```

## Functions
1. **Print a line**  
Write a function that prints a line of 40 hyphens.  

2. **Is it even?**  
Write a function to determine if an integer passed into it is even.  
Note: In prac 6 we did this for if the number was odd, so it's nearly identical.  
Don't copy that code unless you need help. Remember, we should know this now... so notice if you don't know how to do what you've already done before...

3. **Get Non-empty String**  
Write a function to get a non-empty string. That is, you should be able to enter any string as long as it's not "".  
Use this in a program to ask the user for their name using your function...  
Then use the _same_ function for getting their birthplace, and then display a message like: 
    ```
    Hi Martin from New Zealand!
    ```
    So, if you need to use the same function for getting two different things and you want the user to know what you're asking, then you might need a function that can be customised... which is one thing we use _parameters_ for.  

    Note also, that a program that uses a function means we need a main function as well.  

    A good general principle is that you should never write programs that use only one function.  
    If you're using a function like this, then you also want a main.  
    If you only have main, then you don't really need it (but there's nothing wrong with a program that's entirely in a main).  


## Lists

4. **Number List**  
Write a program that asks the user for a minimum and maximum number, then generates a list of integers between those two numbers, then prints it:  
The maximum number must be greater than the minimum.  
Note: **Never** use variable names that are the same as Python built-ins, e.g. `max`, `sum`, `print`, etc.  

    ```
    Minimum number: 10
    Maximum number: 9
    Your maximum must be greater than 10
    Maximum number: 0
    Your maximum must be greater than 10
    Maximum number: 17
    [10, 11, 12, 13, 14, 15, 16, 17]
    ``` 

5. **Subject List**  
Write a program to ask the user for their subject codes until they enter a blank one.    
(Are you getting good at spotting words like 'until' and recognise that's the definite iteration pattern?)  
All valid subject codes contain 6 characters, so reject any invalid subject code and ask again if needed.  

    When you have a list of subject codes, print them in sorted order and tell them how many subjects they have.  
    Then, tell them if they are cool or not... In the lecture notes, we determine if a student is cool based on whether they do CP1401 :)  

    ```
    Enter subject code: CPaoirsetnrsatien
    Invalid subject code
    Enter subject code: C-P
    Invalid subject code
    Enter subject code: MA1020
    Enter subject code: CP1401
    Enter subject code: CP2403
    Enter subject code: CP1406
    Enter subject code: 
    You do these 4 subjects: 
    MA1020
    CP1401
    CP2403
    CP1406
    You are cool
    ```

    Note: As we've tried to both teach and demonstrate, it is highly valuable to get into the habit of **iterative development**.  
    So here, rather than getting the whole thing working in one go, leave out the error-checking until the main part of the program works...  
    _Then_ add error checking using the normal pattern you know and love.

## Strings

6. Processing Strings  

COMING SOON...


## All Together Now
IT@JCU are expanding into the coffee business, and of course they need a Python program to help them, and they need you to write it...

This program includes lists, functions, decision structures, repetition structures and the usual input and output.  
As always, the point is to apply what you have learned in terms of "best practice" (as best you know to date) and use the most appropriate code constructs to solve the problem.

We want a coffee ordering program with a menu, a fixed list of valid coffees to check user orders against, and to print the instructions for making the selected coffee.  
Of course we want to be able to drink our coffee (virtually), and because some people can't decide, we'd like to be able to choose randomly from the menu.

In the functions lecture, Barista Lindsay showed you how to make coffee using 4 'functions'. This program will use those... so make sure you've watched that video.  

### Sample Output
```
Welcome to the IT@JCU Coffee Shop
(O)rder - (D)rink - (R)andom choice - (Q)uit
>>> W
Invalid option
(O)rder - (D)rink - (R)andom choice - (Q)uit
>>> d
Oh... where's my coffee?
(O)rder - (D)rink - (R)andom choice - (Q)uit
>>> o
Please choose from: 
Flat White - Espresso - Long Black - Babyccino - ? Black
Invalid order
? Long black
Here's how to make Long Black: 
- Turn on grinder
- Insert portafilter into grinder
- Grind beans into portafilter
- Add hot water to cup

(O)rder - (D)rink - (R)andom choice - (Q)uit
>>> d
Mmmm, nice Long Black
(O)rder - (D)rink - (R)andom choice - (Q)uit
>>> r
Here's how to make Espresso: 
- Turn on grinder
- Insert portafilter into grinder
- Grind beans into portafilter
- Insert full portafilter into group head
- Press shot button

(O)rder - (D)rink - (R)andom choice - (Q)uit
>>> d
Mmmm, nice Espresso
(O)rder - (D)rink - (R)andom choice - (Q)uit
>>> o
Please choose from: 
Flat White - Espresso - Long Black - Babyccino - ? flat WHITE
Here's how to make Flat White: 
- Turn on grinder
- Insert portafilter into grinder
- Grind beans into portafilter
- Insert full portafilter into group head
- Press shot button
- Fill milk jug
- Steam milk until nice microfoam and up to temperature
- Pour steamed milk into cup...
- Carefully

(O)rder - (D)rink - (R)andom choice - (Q)uit
>>> d
Mmmm, nice Flat White
(O)rder - (D)rink - (R)andom choice - (Q)uit
>>> r
Here's how to make Flat White: 
- Turn on grinder
- Insert portafilter into grinder
- Grind beans into portafilter
- Insert full portafilter into group head
- Press shot button
- Fill milk jug
- Steam milk until nice microfoam and up to temperature
- Pour steamed milk into cup...
- Carefully

(O)rder - (D)rink - (R)andom choice - (Q)uit
>>> q
Thanks for drinking coffee
```

As always, start with **planning**.  
As you look at the description and the sample output, think about:
- nouns (variables)
- verbs (processing, functions)
- sections, including repeated tasks (functions)
- types (strings, lists, etc.)

You should see that each of the functions in the coffee making video will be a function :)  
You should remember that main should "look like the whole program", that is, main should generally consist of function calls (high level overview tasks), and  
You should be able to clearly follow how the program runs by reading just the main function.
You should recognise that when you display the coffees and when you check for a valid coffee order, you're working with a list of valid coffees


# Re-Revision Practice

In checkpoint 1 you wrote the programs below (modified based on our current progress).  
Revisit these and rewrite them for practice.  
As you do, think about enhancing them with functions (where meaningful) and maybe lists.

Note: We do NOT want you whacking in functions that are poor design -  
e.g. violating SRP like a function that calculates _and_ prints.  
Also, remember to include a main function if you use any other function in your program.  
When you're practising, always follow best practice!   
  
See the new comments in each one for suggestions.
  
## Input, Processing, Output

1. Write a program that calculates a new value based on an original value and a (percentage-like) increase or decrease.  
Example:

- Original: 100, Change: 0.05, Result: 105
- Original: 50.5, Change: -0.1, Result: 45.45

> This program could use a function to "calculate" (think verb phrase) the result.

## Decision Structures

2. Ask the user for the time of day (0-23 hours) until they enter a negative.  
Then print a list of all the hours and how many of them were after noon:  

> (This program is quite different from checkpoint 1)

3. Coffee orders made simple.  

- Ask the user for white or black coffee  
- Ask for their chosen size: small, medium or large
- Then print the cost: For Black, Small = $3, Medium = $4, Large = $5. White coffee costs $1 more per size.  
- If a user makes a mistake with their order, just pick the more expensive option :)  

> For this program, you could have a function that gets the coffee order, not allowing mistakes.  
> You could have a function that calculates the cost based on the two parameters the user chose.


## Repetition Structures

5. Write a program to ask the user for a low value and a high value, then print all of the integers between those values inclusive and show the total of those numbers.  
Example, if the inputs were `10` and `20`, you would print:  

    10 11 12 13 14 15 16 17 18 19 20 totals: 165 

> Do this with a list (much like the earlier question) and use `sum` to calculate the total.
