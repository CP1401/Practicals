# Practical 06 - Functions  

## Important! Learn then Do
Do not attempt this practical without learning from the lectures.  
If you're here trying to complete this practical and you have not watched all of the lecture videos + attempted all of the "do this now" exercises from those, then...  
**Stop and do that now!**  
Go learn what we are trying to teach you - then, and only then - come back and do the practical exercises, using that knowledge.


**All students (internal and external), please submit your prac work via LearnJCU each week by the due date.**  

In your PyCharm practicals project, you should be using a new folder for each prac.  
For this practical, create a new folder called `prac_06` to store all of the files.

Write your answers for the early non-coding questions in a simple text file called `questions.txt`.  

## Quick Questions

1. What is the PyCharm shortcut key for commenting selected line/s of code?
2. What is the single most important design principle for designing functions?
3. What is the Python keyword for returning a value from a function?
4. What are arguments and parameters? What is the difference between them? 
5. What is the Python function call for generating a random number between 1 and 100? 
6. Name 4 functions we've used in the subject so far (functions we've "called").
7. How many grams of freshly-ground specialty coffee did Lindsay make his coffee with in the lecture video?


## Good Names

Consider the code:  
```
age = get_age()
```  

Variables should be named using nouns. `age` sounds like a *noun*, so it's a thing, so it's a variable.  
Functions should be named using verbs. `get_age` sounds like a *verb*, so it's a function.

Good function names usually complete the sentence: "This function will..."  
Examples:  
- This function will `calculate_circle_area`
- This function will `get_age`

Write good names for the following functions:

1. determine a subject grade based on a given total score
2. convert currency from USD to AUD
3. print a report
4. calculate the average of a list of numbers
5. determine if a number is even
6. get a user's salary, making sure that it is not negative


# Python Coding - Functions 

As you do individual work on your computer, if you need help, start by talking to your peers.  
Use Slack to ask questions of others in the class.

## Example
Let's walk through a complete example, from problem description, through problem solving to code and testing.  
Just read along and understand. Do not "do" any of this until you are asked. Read it carefully and make sure you understand.  
 
### Problem Description:
> Firstly, we understand that for some people, things like body image, weight and health can be sensitive issues.  
> There is no intention for the following scenario to be taken personally or thought of in any way that might cause concern.  
> It is a useful scenario for the purpose of breaking a problem into functions, which is why it is used.

According to [cancer.org](https://www.cancer.org/cancer/cancer-causes/diet-physical-activity/body-weight-and-cancer-risk/adult-bmi.html):  
> BMI is used to broadly define different weight groups in adults 20 years old or older. The same groups apply to both men and women.

BMI (Body Mass Index) can be calculated by the formula:

```
weight in kg / (height in m ** 2)
```

Remember "** 2" means "to the power of 2"

The rough weight group categories defined by BMI are:

- Underweight: BMI is less than 18.5
- Normal weight: BMI is 18.5 to 24.9
- Overweight: BMI is 25 to 29.9
- Obese: BMI is 30 or more

The client wants a program that will ask for a person's height and weight, then tell them their BMI and weight category. 

### Algorithm
When we look at the problem, we can break it up into a number of main sections. This is *decomposition*.

- get inputs (making sure they're valid)
- calculate BMI
- determine weight category

Each of these can be implemented using *functions*.  
Our main program algorithm will call the other functions.  

We should notice that getting the weight and getting the height are very similar tasks that could be done with almost no difference, so this is a good situation for a reusable function.  
Like we did in the lecture with `get_valid_age`, we'll pass in parameters to define the low and high bounds of the input.  
Unlike that function, we'll also pass in the prompt so we can customise the function's print/output.

```
function main()
    height = get_valid_number("Height", 0, 3)
    weight = get_valid_number("Weight", 0, 300)
    bmi = calculate_bmi(height, weight)
    category = determine_weight_category(bmi)
    print bmi, category
```

At this point, we have an algorithm that represents the whole program, but does not define any of the details. This is useful, but incomplete.  
Let's define the algorithms for each of the functions now.

For the `get_valid_number` function, we should see that this uses the normal error-checking while loop pattern.  
When a valid number has been entered, we "return" it.
 
```
function get_valid_number(prompt, low, high)
    print prompt
    get number
    while number < low or number > high
        print error, prompt
        get number
    return number
```

For the `calculate_bmi` function, we should see that this is a simple calculation/processing step.  
When a result has been calculated, we "return" it.

```
function calculate_bmi(height, weight)
    return weight / (height ** 2)
```

For the `determine_weight_category` function, we should see that this uses the normal if-elif-else decision structure pattern.  
Again, the job of this function is not to print, but to return the category that has been determined by the decision.

```
function determine_weight_category(bmi)
    if bmi < 18.5
        return underweight
    else if bmi < 25
        return normal
    else if bmi < 30
        return overweight
    else
        return obese
```

Notice that the list of categories at the start was taken from the cancer.org website but we understand boundary conditions and have rewritten the conditions in a better way :).

We could test each of these pseudocode functions by trying them out ("desk checking" them). E.g. if we put a BMI value of 27 into the `determine_weight_category` function, we should get "overweight".

### Code

When it comes to coding functions, you can either write main first and then each function (top-down), or write each function and then put it all together in main (bottom-up).  
There's no right answer, but we're going to do it bottom-up and test our functions one at a time before putting them all together.

Look at how very similar the Python code is to the algorithm for the first function we'll write. This would be nearly the same in any language.

```python
def calculate_bmi(height, weight):
    return weight / (height ** 2)
```

**Do this now**  
Create a new Python file, `example.py` (File > New > Python File)    
**Now, you type this code in**, and **test it**.  
But how do we test a function?  
There are a number of ways, but what we'll do here is write a simple function with some tests in it to see what we get when we call our new calculation function.  

We'll do this for each of the functions, so follow along carefully, won't you?  

Add a simple main program at the top of your example.py program, so it looks like:  

```python
def run_tests():
    bmi = calculate_bmi(2, 60)
    print(bmi)  # This should be 15.0
    bmi = calculate_bmi(1.5, 100)
    print(bmi)  # This should be 44.4


def calculate_bmi(height, weight):
    return weight / (height ** 2)


run_tests()
```

Did that work? If it did, we've successfully written and tested our first function!  
If that did not work, go back and see what you've missed.   

Note that we did not write a complete program, getting valid user inputs and producing lovely outputs. We don't care about that yet; we're focused on writing one good function.  

OK, now let's do the next one. **Type this function in** (under the calculate_bmi function), paying attention to how it works and is designed. Notice also how similar it is to the algorithm.  
Try and write simple and understandable algorithms that match the basic logic without too many extra words or weird things... and you'll find it easier to write simple effective code to match :). 

```python
def determine_weight_category(bmi):
    if bmi < 18.5:
        return "underweight"
    elif bmi < 25:
        return "normal"
    elif bmi < 30:
        return "overweight"
    else:
        return "obese"
```

**Now, see if you can write some simple tests - in the same testing function**.  
Think about this yourself before you try what we have below...

```python
print(determine_weight_category(16.5))  # This should be underweight
print(determine_weight_category(25))  # This should be overweight
```

Notice that in these tests we didn't bother saving the category as a variable. We can just print what the function returns directly.  
Notice also that we tested a boundary condition (25) because that's what good programmers do, right?  
Of course, we should test ALL of the conditions, so **write at least as many tests as there are different outputs now.**

How are you going? If any of this is not making sense, it might be a good idea to go back to the lectures and see what you might have missed in the teaching there.  

Before we write our nicely reusable function for getting valid inputs, how about we try a complete main program without it. We'll then add that function as an enhancement.

**Type this main function at the top of your program**:

```python
def main():
    height = float(input("Height (m): "))
    weight = float(input("Weight (kg): "))
    bmi = calculate_bmi(height, weight)
    category = determine_weight_category(bmi)
    print(f"This BMI is {bmi}, which is considered {category}")
```

To run this, you will need to *comment out* the call to `run_tests()` at the bottom (don't delete it because we might want it again later). Then write a call to `main()` below it.

Run the program and test it with known values, like:  

```
Height (m): 2
Weight (kg): 60
This BMI is 15.0, which is considered underweight
```

Good? As usual, if you're stuck with something, make sure you've followed and understood. If you missed something, go back and re-read the instructions, check your code, and fix it.

So, we've got a complete program, don't we? Nice... but what happens if we use invalid values like height=10 and weight=-50? Is a BMI of -0.5 really OK?  

Looks like we want to error-check those inputs. Both of them. Wait... both of them...? The same way? Like, repeating code? \<insert scream>  

Remember, that any time we're repeating ourselves in code, we should stop and ask if there's a better way.  
Reusable functions to the rescue!

**Now, add the following function, as designed in the algorithm above**

```python
def get_valid_number(prompt, low, high):
    number = float(input(prompt))
    while number < low or number > high:
        print("Invalid input")
        number = float(input(prompt))
    return number
```  

Notice that this function doesn't mention "height" or "weight". It has instead been designed to be generic and reusable. It's reusable for height or weight or age or ... any float! That's why our variable is just `number`. It's a generic and not misleading name.

Now, before we use this in our main program, we should... *test* it.  
Change the last 2 lines of your program so `main()` is commented out and `run_tests()` is back in.  

Then add some tests. You should be able to do this yourself now. Write two calls to the function that get different values and save them into variables, then print those variables.

```python
height = get_valid_number("Height (m): ", 0, 3)
print(height)
weight = get_valid_number("Weight (kg): ", 0, 300)
print(weight)
```

If that worked, go on. Otherwise, fix your function.  
This is important, so we'll say it again. You can't use a broken function! You should not use an untested function. Test it, fix it if needed, then use it.

We're in the final stretch now (\<insert exciting music>).  
You may have noticed that we chose tests that exactly match what we want to use for our main program.  
Comment out the two lines in main that get height and width now, and add the two lines from our tests.    
Change the last two lines of the program so that you're running/calling `main` and let's see it in action:

```
Height (m): 10
Invalid input
Height (m): -1
Invalid input
Height (m): 1.5
Weight (kg): 999
Invalid input
Weight (kg): -1
Invalid input
Weight (kg): 100
This BMI is 44.44444444444444, which is considered obese
```

If you don't have it completed from each of the steps above, [here is the complete example.py program](./example.py) for your reference.

### Things to do

We did quite a number of steps along the way with this example program.  
Here are a few more things to extend it just a bit more: 

- Change the printing of BMI (NOT the calculation) in main so that it only shows 1 decimal place (e.g. 44.4 not 44.44444... as above).
- If you have not done so already, complete your `run_tests` function so that you test each possible weight category (see note below). 
- Add to your main to ask for the person's age using appropriate arguments for the `get_valid_number` function. Use the age in the final output of main.
- Look at your code. Do you see any grey underlines in PyCharm? If you do, move your mouse over them (don't click, just move) and read the popup message. You might see a PEP8 warning - probably a missing line break or space. Press the shortcut key **Ctrl+Alt+L** (Windows) or **Cmd+Opt+L** (Mac) and watch all of your formatting problems get fixed! Smile :)  

#### Note: Test all the things

If you write a program with code that looks something looks like:

```
if condition 1
    do thing A
else if condition 2
    do thing B
else
    do thing C
```

Then there are 3 paths (A, B, C) that could possibly occur.  
To test this properly, you need to write and run *at least* 3 tests, so you see things A, B and C.  
Get into the habit of testing your code systematically and completely.  
**Example/Motivation:**  
Say you had something like:  

```python
value = int(input("Value: "))
if value < 0:
    print("Small value")
elif value > -5:
    print("Big value")
else:
    print("Other value")
```

If you never tested that you could see ALL 3 of "Small", "Big" and "Other", then you might think it works... 
and you wouldn't know that it's broken!

In the BMI question - look at how many possible outputs could occur and make sure your testing covers each one of them.  
You don't need to test every single possible BMI... that would be infinite. 
You need to test each weight category in this case.

# Coding Exercises

Until now, it's been fairly easy to fit our programs into one file. But now that we have multiple functions and each program should usually have a `main` function, we will use separate files for each exercise.   
Write your answers in Python files named as instructed  
At the top of each program, put a short **module docstring comment** with the exercise number/name (copy-and-paste it from here) so you/we know what the program is for later.  
Example:

```python
"""1. Coffee Brew Ratio"""

def main():
    ...
``` 

**Note:** In any questions that ask you to write a function, you are expected to write test code to show that it works as expected. In some cases, you will be told how to test, and in others it is assumed. Get used to writing simple tests, as in our example.  


## 1. Coffee Brew Ratio
File: `coffee_ratio.py`

In practical 1 you wrote an algorithm for calculating a coffee brew ratio based on dose and yield, something like:  

```
get dose, yield
ratio = yield / dose
print ratio
``` 

Here, "ratio" is the number of grams of yield (brewed coffee) per 1 gram of dose (ground coffee), expressed as a float, e.g. 2.5.

[According to La Marzocco](https://au.lamarzoccohome.com/brew-ratios-around-world/):
> Using traditional Italian espresso nomenclature, we’ll refer to a brew ratio of 1:1 (18 grams in / 18 grams out, for example) to 1:2 (18 grams in / 36 grams out) as a “ristretto” espresso; a 1:2 to a 1:3 ratio as a “normale” espresso; and a 1:3 to 1:4 ratio as a “lungo” espresso.

**Write an algorithm** to determine the coffee "style" based on the brew ratio.  
E.g. a ratio of 2.5 (1:2.5) would be a "normale".  
Note: We will consider anything outside the ranges defined above to match the nearest style,   
E.g. 1:0.1 wouldn't be good coffee, but we'd call it a "ristretto" and 1:100 would be dishwater, but let's call it a "lungo".

Now, that looks like the sort of thing we could use a function for in our code, doesn't it?  
We _pass in_ a number like 2.5 and the function _returns_ a string like "normale".  
This is a very common style of function, converting one value to another.

**Write a second algorithm** (it will be very similar, so copy-and-paste then modify) for a **function** that takes in ratio and returns the style.  
Use the above examples as a reference. This is very much like the function for determining a weight category based on a BMI value.  

**Now write this function in Python**. Think of a good verb-phrase name.
  
Next, like we did with the example, let's write another function to test it:

```python
def test_coffee():
    style = determine_coffee_style(1)
    print(style)  # This should be ristretto
    style = determine_coffee_style(2)
    print(style)  # This should be normale
    style = determine_coffee_style(13.5)
    print(style)  # This should be lungo
``` 

Notice that we tested at least one of each style and some boundary conditions. (You could do more complete testing if you want.)

**Now write a main program** that asks the user for the dose and yield, works out the brew ratio then uses your function to determine the coffee style.  
Remember that `main()` should always be your first function in any program file.  
Note: `yield` is a Python statement (keyword) so you can't use it as a variable.  
As a general rule, never use Python keywords as variables, even if you're allowed to (e.g. `sum` is a Python function but you're allowed to use it as a variable name... but don't.)

Sample output:
```
Dose: 18
Yield: 36
1:2.0 is considered normale
```

How did you go? Got it? Use the examples above and the teaching in the lectures if you get stuck on anything. Ask for help if you still need more support.  

One more thing. In the BMI example program, we had a nice helpful function for getting a valid number.  
Copy and paste this into your program (near the bottom) and then use it (call it) when you get the dose and yield.

Your final program should look quite a lot like our BMI example. 
Don't forget that our examples are some of the most helpful resources you have. **Use them!**  

## 2. Parity
File: `parity.py`

One of the most important points with this question is about function *naming*. In each case, think about what is the most meaningful name you can come up with.  
Remember: "This function will..." 

**Part 1**  
Write a function to _print_ the parity of a number.  
Parity is the number % 2  and is either 0 or 1.   
E.g. the parity of 4 is 0 and the parity of 41 is 1.  

**Part 2**  
After you have written this and tested it (e.g. with 4 and 41), write a new function that _returns_ the parity instead of printing it.   

**Part 3**  
After you have written and tested that one, write a third function that returns a Boolean for whether the value passed in is odd.  
Recall from the lecture, that an excellent and common convention for naming Boolean-returning functions is to start their names with is.  
Example, the built-in string method `isupper()` determines if a string is uppercase.  

When you have finshed all 3 of these functions, review their names and see how you did.  
Are the names clear and unambiguous? Would a programmer know how to use these functions based on their names?

## 3. JCU Grades
File: `jcu_grades.py`

According to [JCU Policy](https://www.jcu.edu.au/policy/learning-and-teaching/learning-teaching-and-assessment-policy), if you score 86% in a JCU subject, you will receive an HD grade; 40% will get you an N, etc.

Write a function that takes a subject total score (0-100) and returns the corresponding JCU grade.

Test it, then write a program that asks the user for their score and prints their grade until they enter a score of < 0.

**After** you have finished and tested that program, add to it (same main) so that the program asks the user for a number of scores, then generates that many random scores and shows their grades.  
Example output: 

```
Score: 65
The score 65.0 is C
Score: 89.5
The score 89.5 is HD
Score: -1
How many random scores: 5
16 = N
15 = N
75 = D
53 = P
13 = N
```

You may notice that the display of scores and grades are different in the first part compared to the second (random).  
Remember **SRP** - that functions should do one thing. So, it's not the function's job to format the score or the =/is,
but rather it the function has ONLY ONE JOB and that's to... determine the grade.  
How the grade is used, printed, or whatever, is up to the code that calls this function.


## 4. Add Functions to Previous Pracs
File: `previous_pracs.py`

Rewrite each of the following programs from your previous practicals with functions.  
Do not rewrite those files, but copy the code into this prac and rewrite it here.  

In each case, think about what sections can logically become functions and what should stay in main.  
In some cases, you may be able to reuse functions that you can share between programs in the same file.

- [Calculate salary for worker level](https://github.com/CP1401/Practicals/tree/master/prac_04#1-error-checking)
- [Print grid(rows, columns)](https://github.com/CP1401/Practicals/tree/master/prac_04#6-nested-loop)


# Practice and Extension

These final sections in practicals are not _required_ to be completed for marks, but you will definitely find benefit in completing them for extra practice and to extend yourself.  
The more practice you do, the more you develop and "lock in" your new skills.  

Create a new file, `practice.py` to complete these tasks in:

## A. Coffee Ratio Calculation
Update your coffee brew ratio program with a new function to do your ratio calculation.

Write a test for it, then use it in your main program. 

## B. Random Coffee
Suppose you have a dodgy espresso machine that's hard to control, so you get a random yield each time you brew.  
Write a new version of your coffee program that asks the user for their dose but sets the yield to a random number between some realistic values that you set.

## C. Reverse Words
Write a function called `print_reversed_words` that takes two string parameters and prints them in the reverse order.   
E.g. calling `print_reversed_words("hi", "ho")` would print `ho hi`
 

# Extension

## i. Coffee Test with Loop

Write another function for testing your coffee style determining function.  
This time, use a loop to run through at least one of each of the styles.  
Try and produce output like the following:

```
1:0.5 is considered ristretto
1:1.5 is considered ristretto
1:2.5 is considered normale
1:3.5 is considered lungo
1:4.5 is considered lungo
``` 

## ii. Steakhouse 2
Write a new version of the [Automated Steakhouse from prac 3](https://github.com/CP1401/Practicals/tree/master/prac_03#example) but:  
Instead of asking the user for their steak style (e.g. medium rare), ask the chef for a number of minutes and print what the style will be (e.g. 1 minute is rare, 20 minutes is burned).  
Think about the functions that make sense, including reusing your function for getting a number. 

## iii. Tax Calculation
 Rewrite the [calculate tax(income) program from prac 3](https://github.com/CP1401/Practicals/tree/master/prac_03#1-tax) but note:  
The calculation function should return 2 values (`total_tax` and `take_home_pay`).   
We did not learn about how to do this in the lecture, but you can return as many values as you want from a function.  
To store these values, use multiple variables, like:

```python
x, y = function_that_returns_2_values()
```  

# Deliverables
This section summarises the expectations for marking in this practical.

`questions.txt` with:

- Quick Questions
- Good Names

`example.py` with updates

Exercises, each in their own file:

- `cofee_ratio.py`
- `parity.py`
- `previous_pracs.py`
- `jcu_grades.py`
