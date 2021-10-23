# Practical 09 - Coding Checkpoint 2 & Strings

Solutions for these checkpoint questions are provided as 
worked solution demonstration videos.  
Please do your own solutions before watching ours!

### Use Docstrings
Please watch the checkpoint 2 video lecture on docstrings before starting this work.  

For each of your functions, write a brief function **docstring**. Docstrings, like all comments, should be written in the imperative mood, e.g., "Print" not "Prints".  

Here's a good example for a function that checks to see if a password is valid:

```python
def is_valid_password(password):
    """Determine if password is considered valid or not."""
    if len(password) < 6 or " " in password:
        return False
    return True
```

## Functions
Note that a program that uses a function means we need a `main` function as well.  

A good general principle is that you should never write programs that use only one function.  
If you're using a function (like those asked for below), then you also want a main.  
If you only have main, then you don't really need it (but there's nothing wrong with a program that's entirely in a main).  

To make today's practical work easier to identify (and selectively run) but without using lots of separate files, we'll write questions with the "main" code in functions like `question_1()`. 

### 1. Print a line  
Write a function that prints a line of 40 hyphens.  

Call your function to test it from a function called `question_1()`.

### 2. Is it even? 
Write a function to determine if an integer passed into it is even.  
Note: In prac 6 we did this for if the number was odd, so it's nearly identical.  
Don't copy that code unless you need help. Remember, we should know this now... so notice if you don't know how to do what you've already done before...

Write testing code in `question_2()` that shows how this function should work, like:

```python
def question_2():
    some_number = int(input("Number: "))
    if is_even(some_number):
       print(f"{some_number} is even")
    else:
       print(f"{some_number} is odd")
```

### 3. Get Non-empty String 
Write a function to get a non-empty string. That is, you should be able to enter any string as long as it's not `""`.  

In a `question_3()` function, call your new function to ask the user for their name using your function...  
Then use the _same_ function for getting their birthplace, and then display a message like:  
```
Hi Martin from New Zealand!
```

Notice how this works: we can use the same function for getting two different things because we can customise the way the function works using **parameters**.  

## Lists

### 4. Number List  
Write a `question_4()` that asks the user for a minimum and maximum number (ensuring the maximum is greater than the minimum).  
Then generate a list of integers between those two numbers and print it, as shown below.  

Note: **Never** use variable names that are the same as Python built-ins, e.g., `max`, `sum`, `print`, etc.  

```
Minimum number: 10
Maximum number: 9
Your maximum must be greater than 10
Maximum number: 10
Your maximum must be greater than 10
Maximum number: 17
[10, 11, 12, 13, 14, 15, 16, 17]
``` 

### 5. Subject List  
Write a program in `question_5()` to ask the user for their subject codes until they enter a blank one.    
(Are you getting good at spotting words like **'until'** and recognising that's the **indefinite iteration pattern**?)  
All valid subject codes contain 6 characters, so reject any invalid subject code and ask again if needed.  

When you have a list of subject codes, print them in **sorted** order and tell them how many subjects they have.  
Then, tell them if they are cool or not... In the lecture notes, we determine if a student is cool based on whether they do CP1401 :)  

```
Enter subject code: CPaoirsetnrsatien
Invalid subject code
Enter subject code: MA1020
Enter subject code: CP1401
Enter subject code: C-P
Invalid subject code
Enter subject code: CP2403
Enter subject code: CP1406
Enter subject code: 
You do these 4 subjects: 
CP1401
CP1406
CP2403
MA1020
You are cool
```

Note: As we've tried to both teach and demonstrate, it is highly valuable to get into the habit of **iterative development**.  
So here, rather than getting the whole thing working in one go, leave out the error-checking until the main part of the program works...  
_Then_ add error checking using the normal pattern you know and love.


## All Together Now
File: `coffee_orders.py`

IT@JCU are expanding into the coffee business, and of course they need a Python program to help them, and they need you to write it...

This program includes lists, functions, decision structures, repetition structures and the usual input and output.  
As always, the point is to apply what you have learned in terms of "best practice" and use the most appropriate code constructs to solve the problem.

We want a coffee ordering program with a menu, a fixed list of valid coffees to check user orders against, and instructions for making the selected coffee.  
Of course, we want to be able to drink our coffee (virtually), and because some people can't decide, we'd like to be able to choose randomly from the menu.

In the functions lecture, Barista Lindsay showed you how to make coffee using 4 'functions'. This program will use those... so make sure you've watched that video.  

### Sample Output
```
Welcome to the IT@JCU Coffee Shop
(O)rder - (D)rink - (R)andom choice - (Q)uit
>>> C
Invalid option
(O)rder - (D)rink - (R)andom choice - (Q)uit
>>> d
Oh... where's my coffee?
(O)rder - (D)rink - (R)andom choice - (Q)uit
>>> o
Please choose from: 
Flat White - Espresso - Long Black - Babyccino - ? capuccino
Invalid order
? I'd like to confuse you with a double shot half-strength machiato with extra milk
Invalid order
? Long BLACK
Here's how to make a/n Long Black: 
- Insert portafilter into grinder
- Press grind button to grind beans into portafilter
- Distribute grounds
- Tamp grounds
- Insert full portafilter into group head
- Press shot button to pour espresso into cup
- Add hot water to cup
(O)rder - (D)rink - (R)andom choice - (Q)uit
>>> d
Mmmm, nice Long Black
(O)rder - (D)rink - (R)andom choice - (Q)uit
>>> R
Here's how to make a/n Flat White: 
- Insert portafilter into grinder
- Press grind button to grind beans into portafilter
- Distribute grounds
- Tamp grounds
- Insert full portafilter into group head
- Press shot button to pour espresso into cup
- Fill jug with milk
- Steam milk until nice microfoam formed and milk up to temperature
- Swirl milk gently in jug
- Pour milk into cup... carefully, artistically :)
(O)rder - (D)rink - (R)andom choice - (Q)uit
>>> o
Please choose from: 
Flat White - Espresso - Long Black - Babyccino - ? espresso
Here's how to make a/n Espresso: 
- Insert portafilter into grinder
- Press grind button to grind beans into portafilter
- Distribute grounds
- Tamp grounds
- Insert full portafilter into group head
- Press shot button to pour espresso into cup
(O)rder - (D)rink - (R)andom choice - (Q)uit
>>> d
Mmmm, nice Espresso
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
- constants

Consider how to use function:
- You should see that each of the functions in the coffee making video will be a function :)  
- You should remember that main should "look like the whole program", that is, main should generally consist of function calls (high level overview tasks)
- Anyone should be able to clearly understand how the program works by reading just the main function.
- You should recognise that when you display the coffees and when you check for a valid coffee order, you're working with a list of valid coffees.
- You should write simple functions for each step (like in the video). E.g., 
```python
def grind_beans():
    print("- Insert portafilter into grinder")
    print("- Press grind button to grind beans into portafilter")
``` 

## Strings
File: `strings.py`

**This is the second substantial part of this practical.  
Depending on your version of this subject, this practical may be done over multiple weeks.**

Stop here and make sure you have watched the **Strings lecture** before completing this section.  
In that lecture, you were shown what you need to know for these exercises, including good examples very similar to these tasks.  

### 6. Processing Strings  
First, let's see another quick example of using slicing and finding.  
Suppose we have data like:
    
```python
string = "Result = 95%"
```
and we want to extract just the percentage as a number.  
If we know the format will be just like that, we can use:
```python
value = int(string[-3:-1])
```
But what if it might be different, like:
```python
string = "Final Score = 8%"
# or 
string = "Relative Value = 178.3%"
```
In those cases, our overly-simplistic approach would not work.  
    
Ideally, we need a robust way of extracting the data, based on the possibilities the string could be.  
So, in this case, let's assume we want all the characters between the `= ` and the `%` (which would be true in all 3 of these cases).

One way to do this is to `find` the index of the space after the = and then slice all the characters from there to one before the end.  
Since we did this in the lecture, the rest is up to you now...

**Write a program in `question_6()`** that processes this list of strings (copy the data here) and prints the values you extract.
    
```python
data_strings = ["Result = 95%", "Final Score = 8%", "Relative Value = 178%",
                "Something else that's very important = 9.2%", "x = 42%"]
```  
    
**Hint**: Don't try and get your processing/extraction working at the same time as your for loop.  
Pick one string and work on that. When it works, add in your loop to see how it works with the others.  
 
Sample output (keep it simple... but notice what types these outputs are):
```
95.0
8.0
178.0
9.2
42.0
```

Last note: There's no obvious 'meaning' in this data, so you can use generic names.  
You're given _strings_, and you need to extract a _value_ from each.

### 7. Date Strings  
(From the lecture)  
Write a program in `question_7()` to get and display only the year from a date of birth stored as a string like `"13/07/1995"`  
Add a little interest to your program, by asking the user for their DOB, then printing like,  
```
DOB: 13/07/1995
You were born in 1995
You turn/ed 25 in 2020.
```

### 8. Subject Code Strings  
The first 3 characters in JCU subject codes always follow a definite pattern:  
The first 2 characters are the discipline (MA = Maths, CP = IT, etc.) and the next character is the year level.  
Who knows what the last 3 characters mean? :)  

Write a program in `question_8()` that asks for subject codes until the user enters a blank one...   
Hey, sounds familiar... BUT this question does not use lists, so you have to change it!   
After they type each one, print what year level it is and whether it's an IT subject.  

Sample Output (Consider carefully your decision structures here)
```
Enter subject code: CP1401
That is a first-year IT subject.
Enter subject code: MA2403
That is a second-year subject.
Enter subject code: CP5639
That is a Masters or other IT subject.
Enter subject code: PH3456
That is a third-year subject.
Enter subject code: 
```

**Hint**: A nice way to do this is with a single print statement that uses variables.  
You do not want to repeat yourself (DRY), right? So don't use lots of different print statements... just look at what's different (different = variable).  
E.g.,
```python
print(f"That is a {year_string}{it_string} subject.")
```

# Re-Revision Practice

In checkpoint 1 you wrote the programs below (modified based on our current progress).  
Revisit these and rewrite them for practice.  
As you do, think about enhancing them with functions (where meaningful) and maybe lists.

Note: We do NOT want you whacking in functions that are poor design -  
e.g., violating SRP like a function that calculates _and_ prints.  
Also, remember to include a `main` function if you use any other function in your program.  
When you're practising, always follow best practice!   
  
See the new comments in each one for suggestions.
  
## Input, Processing, Output

1. Write a program that calculates a new value based on an original value and a (percentage-like) increase or decrease.  
Example:

- Original: 100, Change: 0.05, Result: 105
- Original: 50.5, Change: -0.1, Result: 45.45

This program could use a function to "calculate" (think verb phrase) the result.

## Decision Structures

2. Ask the user for the time of day (0-23 hours) until they enter a negative.  
Then print a list of all the hours and how many of them were after noon:  

(This program is quite different from checkpoint 1)

3. Coffee orders made simple.  

- Ask the user for white or black coffee  
- Ask for their chosen size: small, medium or large
- Then print the cost: For Black, Small = $3, Medium = $4, Large = $5. White coffee costs $1 more per size.  
- If a user makes a mistake with their order, just pick the more expensive option :)  

For this program, you could have a function that gets the coffee order, not allowing mistakes.  
You could have a function that calculates the cost based on the two parameters the user chose.


## Repetition Structures

5. Write a program to ask the user for a low value and a high value, then print all the integers between those values inclusive and show the total of those numbers.  
Example, if the inputs were `10` and `20`, you would print:  

    10 11 12 13 14 15 16 17 18 19 20 totals: 165 

Do this with a list (much like the earlier question) and use `sum` to calculate the total.

# Deliverables
This section summarises the expectations for marking in this practical.

- `checkpoint_02.py` with programs 1-8
- `checkpoint_02_coffee_orders.py` (All Together Now)
