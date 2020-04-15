# Practical 06 - Functions  

## Important! Learn then Do
Do not attempt this practical without learning from the lectures.  
If you're here trying to this practical and you have not watched all of the lecture videos + attempted all of the "do this now" exercises from those, then...  
*Stop* and do that now. Go learn what we are trying to teach you - then, and only then - come back and do the practical exercises, using that knowledge.


**All students (internal and external), please submit your prac work via LearnJCU each week by the due date for your situation.**  

Write your answers for the early non-coding questions in a simple text file called `questions.txt`.  

## Quick Questions

1. What is the PyCharm shortcut key for commenting selected line/s of code?
2. What is the single most important design principle for designing functions?
3. What is the Python keyword for returning a value from a function?
4. What are arguments and parameters? What is the difference between them? 
5. What is the Python function call for generating a random number between 1 and 100? 
6. Name 4 functions we've used (called) in the subject so far.
7. How many grams of freshly-ground specialty coffee did Lindsay make his coffee with in the lecture video?


## Good Names

Consider the code:  
```
age = get_age()
```  

Variables should be named using nouns. `age` sounds like a *noun*, so it's a thing, so it's a variable.  
Functions should be named using verbs. `get_age()` sounds like a *verb*, so it's a function.

Good function names usually complete the sentence: "This function will..."  
Examples:  
- This function will `calculate_circle_area()`
- This function will `get_age()`

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

BMI can be calculated by the formula:

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

**Type this main function at the top of your program**

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

Looks like we want to error-check those inputs. Both of them. Wait... both of them...? The same way? Like, repeating code? <insert scream>  

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

We're in the final stretch now (<insert music>).  
You may have noticed that we chose tests that exactly match what we want to use for our main program.  
Comment out the two lines in main that get height and width now, and add the two lines from our tests.    
Swap comments for the last two lines of the program so that you're running main and let's see it in action

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

- See if you can change the printing of BMI (NOT the calculation) in main so that it is limited to 1 decimal place (e.g. 44.4 not 44.44444... as above).
- If you have not done so already, complete your `run_tests` function so that it covers each logical possibility of output. 
- Add to your main to ask for the person's age using appropriate arguments for the `get_valid_number` function. Use the age in the final output of main.
- Look at your code. Do you see any grey underlines in PyCharm? If you do, move your mouse over them (don't click, just move) and read the popup message. You might see a PEP8 warning - probably a missing line break or space. Press the shortcut key **Ctrl+Alt+L** (Windows) or **Cmd+Opt+L** (Mac) and watch all of your formatting problems get fixed! Smile :)  

###### CATCH-ALL
`print_reversed_words` – takes two string parameters and prints them in the reverse order.   
E.g. calling `print_reversed_words("hi", "ho")` would print `ho hi`
 
Parity
Write a function to print the parity of a number (parity is the number % 2  and is either 0 or 1). 
E.g. the parity of 4 is 0 and the parity of 41 is 1.
xx maybe do print, then return, then Boolean

###### ...

# Coding Exercises
 
Write all of your answers to the following questions in a single Python file called `programs.py`  
At the top of each program, put a **comment** (starts with a `#`) with the exercise number/name (copy-and-paste it from here) so you/we know what the program is for later.  
Example:

```python
# 2. Miles to Kilometres
number_of_miles = int(input("Miles: "))
...
``` 

## 1. Sth
**Write a complete Python program** that 
Here is the algorithm already done for you in pseudocode:
```
get 
print 
```

**Test** this using meaningful test data that you can understand.  

Remember that you can **comment out** code so it doesn't run by selecting the lines of code (doesn't need to be exact characters, just any part of the right lines) and press `Ctrl+/` (Windows) or `Cmd+/` (Mac).

## 2. 

# Practice and Extension

These final sections in practicals are not _required_ to be completed for marks, but you will definitely find benefit in completing them for extra practice and to extend yourself.  
The more practice you do, the more you develop and "lock in" your new skills.  

Create a new file, `practice.py` to complete these tasks in:


### Extension

 
