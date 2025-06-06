# Practical 03 - Decision Structures

As with each new practical, create a new directory (folder) in your existing practicals project.  
**Do not make a new project!**  
Call your new folder `prac_03` and put all of your practical 3 files in this folder.  
Write your answers for the early non-coding questions in a simple text file called `questions.txt`.  
By now you should be able to use PyCharm easily enough to edit text files.

## Quick Questions

Answer these quick questions in your `questions.txt` file.  
For questions 3-6, calculate the result of the expression using the following as the variable values:

```python
a = 2
b = 3
c = 4
```

1. What is the "not equal to" operator in Python?
2. What is the "less than or equal to" operator in Python?
3. b + c * a > a ** b
4. True or (c ** b - a % b > c ** c)
5. not True and False or True
6. (a * b + c) % 2 == 0

## Patterns

[We have learned 5 common **decision
patterns**](https://github.com/CP1404/Starter/wiki/Programming-Patterns#decision-structures) and when to use them
(the "best tool for the job"):

1. if, no else
2. if, else
3. if, elif, else
4. if, elif no else
5. if, if, if...

**Which pattern** would be the most appropriate choice for each of the following situations:

1. Deciding what coffee to make based on a customer's order (flat white, cappuccino, piccolo, long black, espresso...)
2. Deciding whether to toast a customer's sandwich
3. Recording what foods a customer is allergic to (ask for each allergen)
4. Calculating tax based on income - could be one of several tax brackets
5. Handling the "play again?" question at the end of a computer game level
6. Determining if a frog is poisonous based on its colour
7. Determining if a frog is poisonous based on its colour, tongue length and number of eyes

## Logic Exercise

When asked her 3 children's ages, Mrs. Muddled said that Alice is the youngest unless Bill is, and that if Carl isn't
the youngest then Alice is the oldest.  
Who is the oldest and who is the youngest?

## Note

Before we get on to writing code, we need to highlight a very common error.

When using compound Boolean expressions (sounds fancy doesn't it?) with **and** and/or **or**, you need to make each
side of the expression complete.  
Example:

```
if age < 0 or > 100  # not OK
```

This is NOT OK, because the right side (after the or) is just `> 100`
which is incomplete and cannot be determined.  
In English, we often shortcut this when we speak (e.g. the above could be said "if age is less than zero or greater than
one hundred") – makes sense to us, but in pseudocode and code, you can't take that shortcut.  
You need to restate the variable to make the expression complete so that the code can run (and so pseudocode makes
sense).  
Example:

```
if age < 0 or age > 100	 # OK
```

# Python Coding - Decision Structures

As you do individual work on your computer, if you need help, start by talking to your peers.  
External students are encouraged to use Slack to ask questions of others in the class.

## Example

Let's walk through a complete example, from problem description, through problem solving to code and testing.  
Just read along and understand. Do not "do" any of this, just read it and make sure you understand. Ask your peers if
you need any help.    
Use this example (and the lecture teaching) as a reference when you do your own work.

### Problem Description:

The Automated Steakhouse needs a program to tell customers how long they can expect to wait for their steak.  
The customer has three options: "rare", "medium" and "well-done" - if they enter anything else, they receive an error
message. Rare steaks take 2 minutes to cook, medium steaks take 4 minutes to cook, and well-done steaks require 6
minutes.

When we decompose the problem, looking for nouns, verbs and "decision" words, we can see things like "options" and "if",
so we're going to be using decisions.  
We can see multiple cases/paths and their conditions.  
Also, we can tell that there is a default case - the error message.

What pattern will we use?  
This looks like a menu-style problem and has multiple cases with a default, so...  
It's clearly the **if, elif, else** pattern.

### Algorithm

Notice that in pseudocode we use "else if", not "elif", since "elif" is code specific to Python, and it means "else if".

```
get choice
if choice == "rare"
    display "2 minutes"
else if choice == "medium"
    display "4 minutes"
else if choice == "well-done"
    display "6 minutes"
else
   display error message
```

### Code

```python
choice = input("Steak choice (rare, medium or well-done): ")
if choice == "rare":
    print("2 minutes")
elif choice == "medium":
    print("4 minutes")
elif choice == "well-done":
    print("6 minutes")
else:
    print("Ain't no steak like that here")
```

### Testing

Remember that when testing decision structures, we should use test data to produce each path/output.  
There are 4 possible paths here, so we need to test each one, like:

| Input     | Expected Output               | Actual Output |
|-----------|-------------------------------|---------------|
| rare      | 2 minutes                     | ?             |
| medium    | 4 minutes                     | ?             |
| well-done | 6 minutes                     | ?             |
| anything  | Ain't no steak like that here | ?             |

### Things to do

Create a new Python file, `example.py` (File > New > Python File)    
**Now, you type this code in (don't copy it)**, and **test it** with the planned test values.  
As you type into PyCharm, watch how the IDE helps you complete the task. E.g. when you press Enter after a colon, it
automatically indents.  
You should also try typing your `elif` or `else` statements completely before you indent/outdent and watch to see that
PyCharm automatically puts them in the right position!

**Now, make these changes** to help you understand the code:

- Add another case: "burnt" should take 8 minutes
- Try testing with "Rare" instead of "rare". What happens? Apparently `"Rare" != "rare"`, but you knew that already.

We could handle this using something like:

```python
if choice == "rare" or choice == "Rare":
```

**but** what about `"RARE"`, isn't that also the same thing?

We are going to jump ahead to some string processing and learn to use the `lower()` method...

We can essentially ignore the upper/lower case by converting our choice string to lower case.  
We can either do this for each and every condition, or (better), just when we get the input.  
**Try this** in your code now:

```python
choice = input("Steak choice (rare, medium or well-done): ").lower()
```

So, we get the input string and immediately convert it to lower case, which means inputs like "Rare" or "RARE" or "RaRe"
all become "rare".  
Nice!

Test this and see if it works.

# Coding Exercises

Write all of your answers to the following questions in a single Python file called `programs.py`  
At the top of each program, put a **comment** (starts with a `#`) with the exercise number/name (copy-and-paste it from
here) so you/we know what the program is for later.  
Example:

```python
# 1. Tax
...
``` 

## 1. Tax

The following problem is partly done for you. Complete your parts.

The Python Party wins government at the next election and introduce a simple tax system that works like this:

- If you earn under $100, you pay no tax
- If you earn between $100 and $1000, you pay 5% tax on the total amount
- If you earn over $1000, you pay 10% tax on the total amount

**Write the pseudocode** for this in comments, then copy the code below and complete it.  
Note the use of meaningful constants provided.

First, think of which decision pattern applies.  
There are three mutually-exclusive categories of taxation.  
As you write conditions to determine the category, DO NOT REPEAT questions you already know the answer to.

Make sure to only put your calculation for `take_home_pay` in one spot - it does not need to be repeated in each path.

```python
TAX_RATE_LOW = 0.05  # 5%
TAX_RATE_HIGH = 0.1  # 10%
TAX_THRESHOLD_LOW = 100
TAX_THRESHOLD_HIGH = 1000

print("Python Party Tax Program - Where Tax is a Party")
income = float(input("Income: $"))
# TODO: complete this part of the program here

print("Total tax is: $", total_tax, sep="")
print("Take home pay is: $", take_home_pay, sep="")
```

Note: with a situation like this, you should see that in all cases, you want to end up with three properly-set
variables:

- `total_tax` (if you pay no tax, then $0 is the correct total tax)
- `income` (don't change this from what the user enters)
- `take_home_pay` (this will ALWAYS be income - total_tax)

With that in mind, make sure you **don't repeat yourself (DRY)**.  
Seriously, don't... repeat... yourself!

Here is some sample output for two runs of the program, so you know what to test it with ("known-good" data).

```
Python Party Tax Program - Where Tax is a Party
Income: $10000
Total tax is: $1000.00
Take home pay is: $9000.00
```

```
Python Party Tax Program - Where Tax is a Party
Income: $595
Total tax is: $29.75
Take home pay is: $565.25
```

Again, don't worry about the 2 decimal place currency formatting. We will get to that later.

## Don't Repeat Yourself (DRY)

Hopefully you're starting to "get it" with not repeating yourself.  
*Here's a counter-example to show you what **NOT** to do.*

```python3
score = int(input("Score: "))
if score < 0:  # condition 1
    result = score * 2
    print("Bad score :(")
elif score >= 0 and score < 20:  # condition 2
    result = score * 2
    print("Score is OK.")
elif score > 20:  # condition 3
    result = score * 2
    print("Your score is good!")
print("Double your score is", result)
```

This program works, so what's the problem?

- Remember, we don't _just_ want working code, we want _good_ code!
- condition 2 is only checked if condition 1 is False. if condition 1 is False, this is because score must be not < 0,
  so `score >= 0 ` is redundant. It will _always_ be True. condition 2 should be replaced by just `score < 20`
- condition 3 appears to check if condition 2 was False, which we already know, but because this code uses "elif no
  else" we might just make a mistake like getting the boundary condition wrong. What happens if the user enters `20`?
  **Oops!** The right choice of pattern is important! We can fix this by changing condition 3 to `score >= 20` but then
  we ask a question we can guarantee will always be True when we get to it (since the first 2 were False), so that's
  repeating ourselves. DRY.
- Lastly, in all three paths, we repeat the line `result = score * 2`. Again, this works, but is not good. Since we
  always want to do this, it should go _outside_ the decision structure.

Here's the code with these problems fixed. Ah, that's better :)

```python3
score = int(input("Score: "))
if score < 0:
    print("Bad score :(")
elif score < 20:
    print("Score is OK.")
else:
    print("Your score is good!")
result = score * 2
print("Double your score is", result)
```

### One more thing to do...

**Add this one more tax threshold and rate.**  
If we've designed our algorithm well, using the most suitable decision structure, then this should not take much work.

- If you earn between $100 and $500, you pay 2% tax on the total amount

Add this into your code now and notice how much extra work it took.  
If you had to rewrite or change your decision patterns,
then notice that you could have made it more extensible in the first place... so please revisit the teaching on using
decision structures to locate a value in a range.

> [!NOTE]
> The provided code and CONSTANTS are good, so don't change the main structure of the program.  
> However, you might need to change some of your CONSTANT names to suit this new change above.

### Comment out temporarily

Remember that you can **comment out** code so that it doesn't run by selecting the lines of code (doesn't need to be
exact characters, just any part of the right lines) and press `Ctrl+/` (Windows) or `Cmd+/` (Mac).  
Remember also to do this shortcut again when you're finished so that it looks like normal code again - all programs will
run - before you submit your work.

## 2. Car Insurance

Car rental company Painz determines whether a renter requires special insurance based on their age.    
Applicants under 18 are refused hire altogether.  
Applicants under 25 are required to purchase special insurance.  
Applicants 25 years and over are not required to purchase insurance.

Painz needs you to write a program that gets the applicant's age, and outputs "Insurance required", "Insurance not
required", or "Hire refused" as appropriate.

When you write your decision structure, remember to start at one end of the "number line".  
The only place you should _not_ start is with the "special insurance" (middle) category.  
Don't repeat yourself.

### Testing

In comments below your code, list all the values that you should (and did) test with.  
Remember that we have taught systematic ways to test code, so there should be no guesswork here.

## 3. Simple Password Checker

Write a program that has a secret password stored as a **named constant**, and checks a user's password against it.  
Use string comparison to print either "Access granted" or "Access denied" depending on if the user's password matches
the secret.

## 4. Basketball

[The `if, no else` pattern from our teaching](https://github.com/CP1404/Starter/wiki/Programming-Patterns#if-no-else),
is useful for when you want to do something when the condition is true, but do nothing when it's false.  
You do not need an `else`, you just do nothing when the condition is false.

Write a Python program to determine someone's basketball shooting percentage.

Ask the user for the number of shots attempted and the number of shots made.  
Notice that we have
a [style guide naming pattern for "number of ..." variables](https://github.com/CP1404/Starter/wiki/Style-Guide#our-word-choices).
Use it.

If a user has a shooting percentage of 50% or higher, then print an encouraging message, as in the sample output below.

Expected Output:

```
Number of shots attempted: 15
Number of shots made: 3
Your shooting percentage is 20.0% 
```

or

```
Number of shots attempted: 15
Number of shots made: 13
Your shooting percentage is 86.7%
That's great!
```

Notice that the encouraging message is either displayed or it isn't.  
There's no `else` path.

The sample output shows the percentage displayed with 1 decimal place.  
You can do this using f-string formatting, like in the example below:

```python
print(f"Value is ${value:.1f}")
```

## 5. Rock of Ages

Ask the user for their age, then tell them something related to their age.

You need to ensure you write your decision structures **efficiently**.  
DO NOT REPEAT questions you already know the answer to.

- *First*, use a single **compound Boolean expression** to test if the age is invalid (not between 0 and 120 inclusive)
  and print "Invalid age" if it's invalid.
- Then, start at one end (highest or lowest) and work towards the other end
- Print your own custom response for at least four different age categories.

## 6. Speeding Fines

[Current penalties for individuals caught speeding in Queensland](https://www.tmr.qld.gov.au/Safety/Driver-guide/Speeding/Speeding-fines-and-demerit-points.aspx)
are:

| Infringement                                                     | Penalty amount | Demerit points |
|------------------------------------------------------------------|----------------|----------------|
| Less than 11 km/h over the speed limit                           | $309           | 1              |
| At least 11 km/h but not more than 20 km/h over the speed limit  | $464           | 3              |
| More than 20 km/h but not more than 30 km/h over the speed limit | $696           | 4              |
| More than 30 km/h but not more than 40 km/h over the speed limit | $1,161         | 6              |
| More than 40 km/h over the speed limit                           | $1,780         | 8              |

Note: the way the government website has written this (and we've copied it) is NOT efficient in terms of decision
structures. This has been written for each condition to stand alone (if, if, if) but we can tell this is mutually
exclusive, so we know a better tool for the job, don't we?

Avoid a 6-month suspension by writing a program to ask for the user's:

- **speed** and the
- **speed limit**

then tell them their fine in dollars (you can ignore the demerit points).

After getting the inputs, you will want to calculate the speed over the limit. You do not want to calculate this again
and again in each condition. DRY.

Before you finish this question, check again for any "DRY" issues.  
Can you improve your code?

## Reflection

In `questions.txt`, answer the following questions based on your experiences in the subject so far:

1. What is something you have done well in this subject that you should **keep doing**?
2. What is something you have **not** done well in this subject that you should **stop doing**?
3. What is something new that you would like to try, or **start doing** to help your learning progress?

# Practice and Extension

These final sections in practicals are _not required_ to be completed for marks, but you will definitely find benefit in
completing them for extra practice and to extend yourself.  
The more practice you do, the more you develop and "lock in" your new skills.

Create a new file, `practice.py` to complete these tasks in:

## Coffee Pour and Grind

As all good baristas know (right, Raven?), the length of time a shot of coffee pours indicates if the grind level is
right:

- 25-35 seconds = OK, leave it
- under 25 seconds = grind finer (so it pours slower)
- over 35 seconds = grind courser (so it pours faster)

Write an algorithm, then a program, to help create a robot that replaces the barista.  
Give it a cool beard, maybe some tattoos and engaging conversation so the customer still feels the love.

## Good morning, good evening and good night.

Write 4 different versions of a time-based greeting program.  
(You will use different decision patterns for some of these, as appropriate.)

In each case, ask the user for the hour of day (0-23).

1. If it is morning, print "Good morning" (otherwise do nothing)
2. If it is morning, print "Good morning"; if night time, print "Good night"
3. Print either: Good morning / good afternoon / good night
4. Print either: Good morning / good afternoon / good evening / good night

## Pool pH

Given pool pH level:

- 7.4 - 7.6 is ideal, no change
- Below 7.4, is too acidic, add soda
- Above 7.6 is too alkaline, add acid

## JCU Grades

[Grades at JCU work like this](https://www.jcu.edu.au/students/exams-and-results/subject-results-explained) depending on
your final percentage for a subject.

I think you know what to do...  
Write a program to tell a student what their grade is based on their input subject percentage.

| Grade | Percentage |
|-------|------------|
| HD    | 85%-100%   |
| D     | 75%-84%    |
| C     | 65%-74%    |
| P     | 50%-64%    |
| N     | < 50%      |

## Speeding Fines 2.0

If you do this, don't change your existing submission in `programs.py`, put it in your `practice.py` file.

Upgrade your speeding fines program to include the demerit points as well.  
Ask the user at the beginning for their **bank balance** and **number of points**, then tell them the updated balances
if they lost money or points.

## More...

Review the 5 patterns and the programs you've written. Which programs use which patterns?  
Think of more situations and more programs to write for each pattern.   
Practise the patterns you've used the least by implementing some or all of these.

# Extension

### Divisibility

Write a program that takes two numbers, and prints "Divisible" if the first is divisible by the second, and "Not
divisible" otherwise.

## Steak++

Automated Steak House wants version 2 of their program.

- add a default minimum order time as a constant
- handle the outputs as the extra cooking time plus this minimum, so if the minimum is 3 minutes,
  then a rare steak will take 5 minutes.

You should notice that to handle this properly, you will need to replace your fixed outputs with a calculation (e.g.,
not "2 minutes", but 3 + 2).

# Deliverables

This section summarises the expectations for marking in this practical.  
Please follow the [submission guidelines](../README.md#submission) to ensure you receive marks for your work.

**Files required:**

`questions.txt` with:

- Quick Questions
- Patterns
- Logic Exercise
- Reflection

`example.py` with updates

`programs.py` with:

- Tax
- Car Insurance
- Simple Password Checker
- Basketball
- Rock of Ages
- Speeding Fines
