# Practical 04 - Decision Structures 

**All students (internal and external), please submit your prac work via LearnJCU each week by the due date for your situation.**  

Write your answers for the early non-coding questions in a simple text file called `questions.txt`.  


## Quick Questions

1. What is the PyCharm keyboard shortcut for commenting (out/in) a selection of code? 
2. What are the two kinds of loops available in Python?
3. What is a "sentinel" (when dealing with loops)?
4. What is wrong with this variable name: `nothingWrong` 
5. What are augmented assignment operators?	

### range

*a)* Add a new heading "Loop outputs" to your questions.txt file, then:  
Write the output of each of the following `for` loops that use `range`:

```python
# 1.	
for i in range(6):
    print(i, end=' ')

# 2.	
for i in range(33, 39):
    print(i, end=' ')

# 3.	
for i in range(17, 11, -1):
    print(i, end=' ')

# 4.	
for i in range(1, 11):
    print(i % 2, end=' ')

# 5.	
for i in range(10, 0, -2):
    print(i ** 2, end='>')
```

Then, when you have finished writing your output - not before! - copy the code into a Python program and run these loops to check your answers.

*b)* Add a new heading "Range values" to your questions.txt file, then:  
Write the range statements (just range and parameters, not the whole loop) equivalent to the following lists of numbers:

 1.	[0, 1, 2, 3, 4, 5]

 2.	[1, 5, 9, 13]

 3.	[3, 2, 1]

 4.	[7, 4, 1, -2, -5]


## Patterns
We have learned that there are 2 main **repetition patterns** and when to use them (the "best tool for the job"):

- definite (for loops)
- indefinite (while loops)
  
**Which pattern** would be the most appropriate choice for each of the following situations: 

1. Error-checking user input, looping until they enter a valid response
2. A menu with several options including 'quit'  
3. Displaying all of the months in a year
4. Printing 5 random numbers
5. Printing n random numbers, where n is a user input 


## Logic Exercise

There are three boxes which each contains two marbles: 

- one has two white, 
- one has two black, and 
- one has one white and one black marble.   

Each of the boxes also is labeled as to its contents, but each label is _incorrect_.  
What is the fewest number of marbles you could remove from the boxes and look at in order to definitely determine the contents of all three boxes?

*Note*: This is a very interesting exercise, and one you might not get correct without thinking about it carefully (of course).  
*Hint*: Make sure you are using all the information you have been provided with, and think about which is the best choice to start with.

# Python Coding - Decision Structures

## Example
Let's walk through a complete example, from problem description, through problem solving to code and testing.  
Read along and understand. Do not "do" any of this, just read it and make sure you understand, until you get to the section that asks you to do something.    

Often, it is impossible for a program to proceed correctly if the user has entered an invalid value.  
A simple and general pattern for validating user input has been taught in class and is below.  
NOTE: When you see *"general patterns"* in programming, you need to learn these, as you will be reusing them again and again.  
There may be other ways, but the general patterns are usually the best in most situations.  
Pay attention to patterns like this!

```
get input
while <input is not valid>
     display error message
     get input
<do something with input> (at this point, we know that the input entered is valid)
```

### Problem Description:

In this example, we want to ask for the user to enter the month of their birthday as a number (so only a month between 1 and 12 is valid), 
then we will print each of the months of the year up to their birth month.

Sample output:
```
Enter your birth month: -1
Invalid month
Enter your birth month: 13
Invalid month
Enter your birth month: 4
1 2 3 4 
```

### Algorithm

If we analyse the description, we should see that:

- we have two loops
- the first is an error-checking loop, which we can see because the month needs to be "valid"
- the second is a loop that prints "each" of the months up to the input month

We should recognise the type of loops we need: 

- the first will repeat *indefinitely* - until we get a valid month, or "while" the birth month is bad
- the second will repeat *definitely* - from 1 up to the birth month

Note: Don't forget to make use of our useful [Guide to Good Pseudocode](https://github.com/CP1404/Starter/wiki/Pseudocode-Guide). It's useful for how to do things like this...
```
get birth_month
while birth_month < 1 or birth_month > 12
    display error message
    get birth_month

for count from 1 to birth_month
    display count
```

### Code

```python
birth_month = int(input("Enter your birth month: "))
while birth_month < 1 or birth_month > 12:
    print("Invalid month")
    birth_month = int(input("Enter your birth month: "))

for count in range(1, birth_month + 1):
    print(count, end=" ")
print()
```

Notice again, like last week, that we can not shortcut the condition – it is:
	`while month < 1 or month > 12:`
not:
	`while month < 1 or > 12:`

Notice another thing...  
The pseudocode is very similar to the code, but it does not need to be exact.  
We do not need to specify things like the `+ 1` or `end=" "` or the last `print` because those aren't fundamental parts of solving the problem.  

### Testing

To test this kind of input validation program, we need to do the usual:

- Test the normal situations
- Test the abnormal situations 
- Test the boundary conditions

So, for our month number checking loop, we should check with values:

- 5 (first, just try it with something valid in the first instance - we should get no loop)
- 1 and 12 (boundary conditions - which should be valid months)
- 0, 13 (just outside the boundaries)
- and we should test with looping no times (as we did first) and many times, not just once. 

### Things to do

Create a new Python file, `example.py` (File > New > Python File)    
**Now, you type this code in (don't copy it)**, and **test it** with some other values.  
The reason you want to _type_ instead of _copy_ this code is because it helps you learn to use the IDE (e.g. use autocomplete!), 
type code accurately, and develop an eye for detail.

Now update your program as follows:  

- Print whether the birth month is in the first or second half of the year
- I spy some "magic numbers"... While it's unlikely that we'll need to change 1 or 12, we are repeating them.
Replace these literals with named CONSTANTS.
- When you've got the above working, use these constants in the prompt, so it would print like:
`Enter the month number (1-12): `  
Note: This is a good case for some more string formatting. Here are a few options to achieve a string like that.  
Which do you like best? 

```python
# Using the format method:
month = int(input("Enter the month number ({}-{}): ".format(MINIMUM_MONTH, MAXIMUM_MONTH)))

# Using string concatenation and explicit type conversion 
month = int(input("Enter the month number (" + str(MINIMUM_MONTH) + "-" + str(MAXIMUM_MONTH) + "): "))

# Using f-strings - only introduced in Python 3.6
month = int(input(f"Enter the month number ({MINIMUM_MONTH}-{MAXIMUM_MONTH}): "))
```

There's also old-fashioned %-formatting, but it is limited as to the types it supports and is not recommended.  
You might find examples that use %-formatting online, but should avoid this generally.

Note that you cannot simply use commas here like you do in `print`, because `input` does not accept multiple arguments unlike `print`. 


# Coding Exercises
 
Write all of your answers to the following questions in a single Python file called `programs.py`  
At the top of each program, put a **comment** (starts with a `#`) with the exercise number/name (copy-and-paste it from here) so you/we know what the program is for later.  
Example:

```python
# 1. Error Checking
number_of_miles = int(input("Miles: "))
...
``` 

## 1. Error Checking

**Write a complete Python program** to print an employee's salary based on their "worker level". 
Ask the user for their worker level, and error-check this with an appropriate loop to make sure it is between 1 and 10 inclusive.  
When you have a valid entry, print their salary, which is their worker level multiplied by $5000.  

The algorithm will be very similar to the error-checking example above.
 
Use string formatting to make your last output look like currency, e.g.

```python
print("With worker level {}, your salary is ${:,.2f}".format(worker_level, salary))
```

*Sample Output:*
```
Worker level: 0
Invalid worker level
Worker level: 11
Invalid worker level
Worker level: 7
With worker level 7, your salary is $35,000.00
```

**Test** this using meaningful test data that you can understand.  

You will use this error-checking pattern a lot, so get used to it.  

Remember that you can **comment out** code so it doesn't run by selecting the lines of code (doesn't need to be exact characters, just any part of the right lines) and press `Ctrl+/` (Windows) or `Cmd+/` (Mac).

## 2. Number Sequences

Most of the programs in this part are fairly small, so we've combined them into one question with parts:  
 
a.	Write a loop that displays all of the odd numbers between 1 and 100 with a line break between each one.  
b.	Write a loop that displays all of the Summer Olympic years (i.e. every 4 years) between 1896 and today, with a space between each one.  
c.  Write one more loop that represents a meaningful sequence. Explain your chosen sequence in a comment.

## 3. Menus

Not sure how to write menus?  
Think about what you've learned and what pattern best applies.  
Remember we have a [helpful guide to Programming Patterns](https://github.com/CP1404/Starter/wiki/Programming-Patterns#menus). It's very helpful.

Write a program that prints smiley and frowny faces until the user quits.
The user should see a menu like this:
    (S)miley
    (F)rowny
    (Q)uit
Make the program print a smiley face (if they press 's'), a frowny face, or an error message ("Invalid choice") depending on their choice.   
When the user quits, print a farewell message.  

Remember that one of the first things to do when analysing a problem like this is to decide on *definite* vs. *indefinite* repetition.  
Get into the habit of asking yourself that question every time.

## 4. Accumulation

We learned the "accumulation pattern" for calculating running totals in class, and now we'll try it with both definite and indefinite loops.

### Examples/Patterns
Some general patterns for calculating a running total from user input are as follows.  
Each of these patterns has a different purpose and usage.  
Each algorithm pattern is described below using pseudocode.  

#### A. Sentinel

```
SENTINEL = -1
total = 0

get value
while value != SENTINEL
    total = total + value
    get value	
```

You would want to use a *sentinel* when: 

- you don't how many values there will be beforehand; 
- there is some obvious invalid value you can use to be the sentinel and mark the end.

E.g. calculating the average age of a line of people, where you don't know how many there are beforehand (you can use -1 for the sentinel).

#### B. Ask-the-user-to-quit 

Note that this pattern uses a Boolean variable to control the loop.

```
total = 0

is_finished = false
while not is_finished
    get choice
    if choice is to quit
         is_finished = true
    else
         get value
         total = total + value	
```

You would use the *ask-the-user-to-quit* pattern when: 

- you don't how many values there will be beforehand; but 
- there is no particular value that could mark the end of the sequence. 

E.g. calculating the total net worth of a group of people of an unknown size - you can't use a sentinel, because net worth can be positive (more assets than liabilities), zero, or negative (more liabilities than assets).


#### C. Definite count

```
total = 0

get count
repeat count times
    get value
    total = total + value
```

You would use the *definite count* pattern whenever the number of values can be entered beforehand.

E.g. calculating the average test score of the class - we know how many students there are beforehand.

*Now it's your turn...*

### Average Age
Write a program to calculate the average age of a group of unknown size.  
Use the sentinel pattern from above. Hint: you will need to keep track of the total age, and the number of people, separately.

### Smileys Count
Add to your smiley/frowny program so that when the user quits the program tells them how many smileys and how many frownies they printed. (Don't keep track of invalid choices.)

### Total Numbers
Write some code that asks the user for a number of repetitions, then asks for that many numbers and adds them up.  
(Is this definite iteration - we know how many times it will run, or indefinite - we don't know?)  

Sample output would look like:
```
How many numbers do you want to add up? 3
Enter number 1: 7
Enter number 2: 3
Enter number 3: 15
The total of those 3 numbers is 25
```

## 5. Guessing Game
In the lecture, you were given an example like:
```python
SECRET = 6
guess = int(input("Guess a number: "))
while guess != SECRET:
    print("Guess again!")
    guess = int(input("Guess a number: "))
print("You got it!")
```

Make this more interesting by (do each of these *one at a time* before moving on):

- Count the number of times the user guesses, so the program will output something like: `You got it in 3 guesses!`
- Give the user feedback about their guess, so they know if they need to try something higher or lower. 

Example:
```
Guess a number: 3
Higher
Guess a number: 8
Lower
Guess a number: 6
You got it in 3 guesses!
```

See the extension section for a challenge to make this game more gamey :)

## 6. Nested Loops

Loops that are within other loops are called "nested loops". They are commonly used for grid-like situations.  
In the lecture, we saw the example:

```python
for round_number in range(1, 4):
    for name in ["Miles", "Ella", "Chet"]:
        print("Round", round_number, "-", name)
    print("---------------------")
```
(Noting that this uses a list, which we haven't learned about yet - but you can hopefully see how it works.)  

Write a program that asks the user for a number of rows and columns, then prints the numbers to mach, like:

```
Rows: 3
Columns: 7
0 1 2 3 4 5 6 
0 1 2 3 4 5 6 
0 1 2 3 4 5 6 
```

# Practice and Extension

These final sections in practicals are not _required_ to be completed for marks, but you will definitely find benefit in completing them for extra practice and to extend yourself.  
The more practice you do, the more you develop and "lock in" your new skills.  

Create a new file, `practice.py` to complete these tasks in:

## Loopiness
Write a loop that continually asks you for any string and then prints it, until you just press Enter (the empty string is ""). E.g. you type bob, it prints bob, you type hello, it prints hello, you press Enter, it stops.  
(This is indefinite iteration - we don't know how many times it will run.)

## Turn-on
Write a program that asks the user to enter either "on" or "off", and error-check this input until they choose one of these.  
Then print either "the light is on" or "the light is off".
Note: Think about your condition carefully before you run your program to test it.


# Extension

#### 1. Times Tables
Write a program to generate the 15*15 multiplication table.  
To get the spacing nice, note that `"{:4}".format(number)` will make `number` take up four spaces.

```
   1   2   3   4   5   6   7   8   9  10  11  12  13  14  15
   2   4   6   8  10  12  14  16  18  20  22  24  26  28  30
   3   6   9  12  15  18  21  24  27  30  33  36  39  42  45
   4   8  12  16  20  24  28  32  36  40  44  48  52  56  60
   5  10  15  20  25  30  35  40  45  50  55  60  65  70  75
   6  12  18  24  30  36  42  48  54  60  66  72  78  84  90
   7  14  21  28  35  42  49  56  63  70  77  84  91  98 105
   8  16  24  32  40  48  56  64  72  80  88  96 104 112 120
   9  18  27  36  45  54  63  72  81  90  99 108 117 126 135
  10  20  30  40  50  60  70  80  90 100 110 120 130 140 150
  11  22  33  44  55  66  77  88  99 110 121 132 143 154 165
  12  24  36  48  60  72  84  96 108 120 132 144 156 168 180
  13  26  39  52  65  78  91 104 117 130 143 156 169 182 195
  14  28  42  56  70  84  98 112 126 140 154 168 182 196 210
  15  30  45  60  75  90 105 120 135 150 165 180 195 210 225
```

#### 2. Random Secrets
See if you can figure out how to make your guessing game random, so it's not always whatever the SECRET constant is set to.  
Do this by:

- Open the Python Console (down the bottom in PyCharm)
- Type `import random`
- Type `help(random.randint)`
- Armed with that information, write code to generate a random number.

Quick note: Before you start _using_ the random number as a secret, you need to know that your program is generating it properly, so just print it as soon as you've generated it to check this out. 

Then, when you have that working, extend the program so it has minimum and maximum (constants) that are used in the prompts and generating the random secret number.

#### 3. Loopy Loops
Write a new version of your nested loops program that runs like:

```
Rows: 3
Columns: 7
1 1 1 1 1 1 1 
2 2 2 2 2 2 2 
3 3 3 3 3 3 3
```

#### 4. Seriously Loopy

Write a program that works like the output below.  
Hint: use mod (%)
```
Rows: 7
Columns: 10
0 0 0 0 0 0 0 0 0 0 
1 0 1 0 1 0 1 0 1 0 
1 2 0 1 2 0 1 2 0 1 
1 2 3 0 1 2 3 0 1 2 
1 2 3 4 0 1 2 3 4 0 
1 2 3 4 5 0 1 2 3 4 
1 2 3 4 5 6 0 1 2 3 
```

# Deliverables
This section summarises the expectations for marking in this practical.

questions.txt with:

- Quick Questions
- range a) output &  b) parameters
- Patterns
- Logic Exercise

programs.py with:

- Birth Month (updates from example)
- Error Checking
- Number Sequences: a, b, c
- Menu for Smiley/Frowny
- Accumulation: Average Age, Smileys Count, Total Numbers
- Guessing Game
- Nested Loops
