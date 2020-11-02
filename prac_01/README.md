# Practical 01 - Problem Solving and Algorithms

**Welcome to practicals!**

If you haven't read the introduction to pracs and marking, please [read this now](../README.md).  
**Note: All students (internal and external), please submit your prac work via LearnJCU each week by the due date.**


## Community
It's a good idea to start getting to know your IT@JCU community a bit more...  

In lecture 1, we established that it was **not OK** to work together with others on your assignments for this subject, including the simple rules:  
- Never give someone a copy of your work
- Never get a copy of someone else’s work
- This includes looking at theirs or having someone look at yours

You have to do your own work in order to achieve the learning outcomes.  
However, it's still really helpful and good practice to work with others to understand problems and to discuss solutions.  
You **are allowed** to talk with others about these things... you just can't go too far.  
Communication is a big part of IT and it helps to know a little about who you are communicating with. 

So, we're going to do this together **on Slack**.  
*Introduce yourself in Slack* including your name and what you like that starts with the same first letter (e.g. "I'm Yasmin and I like yachting") and also add where you are studying from.


Record your answers for the below questions in a simple text file, `questions.txt`.

## Logic Exercise

Sometimes in our learning, we will have non-IT-based exercises to help us with problem solving in any context. The emphasis is on developing skills that will help you approach new problems and work towards solutions.   
These will not be silly trick riddles, but puzzles with logical, deducible answers.   
The goal is **"to reach a conclusion by reasoning"**.  
One of the important factors in attempting these questions is to really analyse the question and the information given (or not given) in the question without making inappropriate assumptions. This is a valuable skill in IT and programming.  

If you are ever working in a group on these and you already know the answer (or you figure it out quickly), please help the others in the group by NOT just saying the answer. Maybe give appropriate guidance if needed so that others can work it out themselves and learn through the process.  

**Here's our first one...**

-   Brown, Jones and Smith are three friends.
-   One of them is a project manager, one is a consultant, and the other is a programmer.
-   The programmer, who is an only child, earns the least money.
-   Smith, who married Brown\'s sister, earns more than the consultant.

**What is each person's job?**

## Algorithms

Record your answers to the following questions in your text file called `questions.txt`.  
If creating this file takes you more than 30 seconds, then just start the questions, recording them any way you can.

The following exercises are focused on the logic of algorithms, rather than the exact formatting of pseudocode or flowcharts to describe them.  
We're not really interested in writing programs for these, just the basics of writing a set of understandable and clear instructions.  

### Example
Here's an example of an algorithm (written in simple pseudocode) to determine if it's safe to go out and play based on the sun (uv index):

```
get uv index
if uv index < 5
    go out and play
else
    do not go out and play
```

Notice the first line...  
We can't just say: `if uv index < 5` without knowing what `uv index` is, so we have to get it first. 

### Algorithm with I, P, O 
**Write an algorithm** to calculate the brew ratio of coffee, given the dose (quantity of coffee beans in grams) and the yield (brewed coffee in grams).  
Example: A dose of 18g and yield of 45g is a 1 to 2.5 brew ratio.

This algorithm doesn't have any control structures, but just uses **input, processing and output**.

### Algorithm with Selection
**Write an algorithm** to determine if you can afford to buy an item based on its price and a collection of coins you have in your pocket.

This algorithm should have included the **selection** (or decision) control structure. We will learn more about that soon.

### Algorithm with Repetition
**Write an algorithm** to instruct a teenager how to clean their room. They have lots of things on the floor, and need to pick them up until there are no more things on the floor.

This algorithm should have included the **repetition** (or iteration or loop) control structure. We will learn more about that later.


## Problem Decomposition

For the following 3 problem descriptions, identify the **nouns** and **verbs** (separately) in each.   
You could copy the text and highlight each kind of word in different colours, or write two separate lists.  
(Don't get hung up on the exact details of the words.)   

Then go through the set of nouns and verbs and work out which
ones are irrelevant or duplicated and remove them from the lists.  

See if what's remaining is what you need to know to write an algorithm.

1.  A doctor needs to be able to calculate the total amount of a drug
    that has been administered to a patient. The system will get the
    hourly dosage from the user, as well as the number of hours they
    have been receiving the medicine. The system will then display the
    total for the doctor.

2.  Happy Photos needs a way to calculate the total charge for a
    customer's booking. The system will use the customer's name and the
    date of the booking to make a unique booking id. The hourly
    charge, and number of hours will be entered, and the total charge
    and id code will be displayed.

3.  A road trip planning system will ask the user for the distance
    travelled (in km) and the travel time in minutes. The user will then
    be shown the average speed (in km/hour) over the trip.

When you've decomposed these small problems into their parts, **write algorithms** for each of them using either pseudocode or flowcharts.  
At this stage, we're not too worried about getting the details 'perfect', we just want to get used to problem solving processes.

As you do this, think about what **assumptions** you're making.  
Good assumptions are an important part of IT and problem solving.

Potentially, you found it easier to write the algorithms after the "decomposition" step.  
As problems get bigger, we need to be more systematic about our methods.

## Python and PyCharm
(Individual work now. This section does not need to be submitted.)  

We are not going to write any substantial programs in this prac, but we are going to run PyCharm and see how it works.  

If you have your own computer, you can [follow these instructions to install Python 3 and PyCharm Professional](https://github.com/CP1404/Starter/wiki/Software-Setup) remembering you only need Python and PyCharm. 

Let's start by getting used to working with the PyCharm IDE (Integrated Development Environment).  
Note: Your screens may look different than our images or descriptions below depending on versions used.

1.  Run PyCharm.  
    When PyCharm first starts you should have a window with a link to
    create a new project.

    -   A PyCharm **project** is a folder on the computer that contains
        Python source code files and related resource files to make your
        program run... but it's more than that. Always do your coding in files that are part of a meaningful project.

    -   the **Quick Start** window lists several useful tasks like creating a new project or adjusting the configuration of PyCharm

2.  Click on **Create New Project**. and choose **Pure Python**. PyCharm
    asks you where to store your new project and to choose an
    interpreter.  
    Name your new project (folder)  `cp1401practicals`

    -   the **location** can be changed to any place you have access to. Use a folder that you will be able to find later

    -   use the **... button** to select the location

    -   the **interpreter** is the version of Python we need to run our code on the computer.  
        Use the *existing interpreter* for Python 3.  
        **DO NOT use a virtual environment (venv).** They're cool but we don't
        need them in this subject.

![New project window](../images/01image1.png)

3.  Next, let's add our first source code file to the project.  
    **Right-click** on the project name and select  
    **New > Python File**  
    ![New file](../images/01image2.png)

4.  This opens a window where you can define the name of the file - call
    it **hello.py** and hit the **OK** button. Always give your files
    descriptive names so they're easy to find again.

5.  PyCharm created a new source code file in the project folder and
    opened the editor window:
    ![Editor window](../images/01image3.png)

6.  Let's learn our first shortcut! Press **Shift+Enter** to add a blank
    line below the one you're on (no matter where the cursor is). Nice!
    Now type the famous line:

    ```python
    print('Hello world')
    ```

7.  To **run** this first program, **right-click** in the code
    editor window and select **run**.  
    (If it didn't work, please check for what the problem might be, and ask the nearest person for help if you need.)


### Project Structure: Use one project for all practicals

PyCharm doesn't just work with individual code files, but with *projects*. You now have a project for your practicals, and this is the only one you'll need for all pracs.  
So in order to keep your work organised, you will have one well-named folder (directory) for each prac, with well-named files inside the relevant folder.

Let's get used to following best practice (remember that's one of our goals), and create the first folder...  

Right-click on the project name in the top left and select **New > Directory**  
Name this folder/directory

```
prac_01
``` 

This conforms with Python module/package naming conventions, using underscore_lowercase (no spaces).   
Also, by naming it `01` instead of just `1`, when we get to `prac_10`, our alphanumeric sorting will work as we expect (otherwise, prac2 comes _after_ prac10). 

Now that you have the folder, drag your **hello.py** file into it.

**Do not** create new projects for each separate practical.

**Do** use separate projects for each assignment and any other side 'projects'.

### Example program

For fun, let's now copy all of the code from our [catering calculator example program](https://raw.githubusercontent.com/CP1401/subject/master/cateringcalculator.py) 
(Use Ctrl+click to open links in new tabs)  
and paste that into a **new Python file** with the same name, `cateringcalculator.py`.

**Run it**... play with it, change it, break it, see what happens...  
(Don't worry if you don't understand it yet, we've still got a long way to go.)

# *Intermission*
Because we only have six weeks, our practicals are quite large.  
If you've done all of the above in one sitting - well done!  
Now would be a good time to **take a break** before completing the rest our work.  

Seriously, taking regular breaks helps you to maintain (or restore) a positive and active state of mind so you can work effectively and efficiently.  
Make a habit of it.

## Quick Questions - Variables

1.	Write two variable names that would be valid and well-named.
2.	Write two variable names that would be valid but not well-named.
3.	Write two variable names that would not be valid.
4.	What is the naming convention for variables in Python?
5.	What is a constant? Give an example of when you would use one.
6.	What is the naming convention for constants?

# Python Coding - Input, Processing and Output

## Example
Let's walk through a complete example, from problem description, through problem solving to code and testing.  
Just read along and understand. Do not "do" any of this, just read it and make sure you understand.  
 
### Problem Description:
Leia and her friend Han are enjoying a nice meal at a restaurant when they realise it's a public holiday and there's a surcharge.  
She wants to find out what the cost of the meal will be including the surcharge.  
Leia wants to write a program on her laptop to figure this out but complains that her hands are dirty. Han says, "My hands are dirty too; what are you afraid of?"

When you break it down and remove the irrelevant parts, you can see this is a simple problem that follows the basic pattern:
- Input
- Processing
- Output 

### Algorithm

```
get original_price and surcharge_rate
extra_charge = original_price * surcharge_rate
total_price = original_price + extra_charge
display total_price  
```

We could have done the processing calculation either in one step or two.  
Using more steps with good variable names is usually more readable and extensible, but either way is mostly OK.  
  
Also note that here we have used terms written like `original_price`, valid variable names.  
It's fine if you want to use `original price` or something similar, but doing it like variables means that you can copy-and-paste your pseudocode and then convert it to Python without rewriting your terms.  

Note also that we used the term, `surcharge_rate` and not just `surcharge`.  
We could have used something like `surcharge_percentage`, but if we had used just `surcharge`, we might find it hard to 
remember if it means surcharge like 15% (0.15) or like $15 (amount).  
**Variable names should be unambiguous.**

### Code

```python
original_price = float(input("Original price: $"))
surcharge_rate = float(input("Surcharge % (e.g. 0.15 is 15%): "))
extra_charge = original_price * surcharge_rate
total_price = original_price + extra_charge
print("The total meal price is $", total_price, sep="")
```

### Testing

Just because the code is written, doesn't mean it works, so we need to test it. How?  
Put in some meaningful/easy inputs so you can evaluate if the output matches what you expect.  
E.g. We can easily calculate that 15% of 100 is 15, so a $100 meal with a 0.15 (15%) surcharge should cost $115.

```
Original price: $100
Surcharge % (e.g. 0.15 is 15%): 0.15
The total meal price is $115.0
```

Looks good.

Create a new Python file, `example.py` (File > New > Python File)    
**Now, you type this code in (don't copy it)**, and **test it** with some other values.  
The reason you want to _type_ instead of _copy_ this code is because it helps you learn to use the IDE (e.g. use autocomplete!), 
type code accurately, and develop an eye for detail.


# Coding Exercises
 
Write all of your answers to the following questions in a single Python file called `programs.py`  
At the top of each program, put a **comment** (starts with a `#`) with the exercise number/name (copy-and-paste it from here) so you/we know what the program is for later.  
Example:

```python
# 2. Miles to Kilometres
number_of_miles = int(input("Miles: "))
...
``` 

## 1. Discount Price
**Write a complete Python program** that calculates the discounted price of an item given an original price and a fixed discount of 20%.  
Here is the algorithm already done for you in pseudocode:
```
get original_price
discount = original_price * 0.2
new_price = original_price – discount
print new_price
```

**Test** this using meaningful test data that you can understand.  
Once you have done this, adjust your program so that `0.2` is a **named constant** instead of a **magic number**.  
Test it again.  
Always test your programs after you modify them. You might have broken something.  

### Commenting Out Code
Now that you want to move on to the next exercise, you _could_ start a new file, but just going to keep using the same one.  
However, you don't want to _run_ the old programs as well as the new one, so you can "comment out" the previous program code.  
To do this, select the lines of code (doesn't need to be exact characters, just any part of the right lines) and press `Ctrl+/` (Windows) or `Cmd+/` (Mac).

## 2. Miles to Kilometres

Joseph has recently moved to Australia from the United States. He understands that distances are given in kilometres rather than the miles he is used to.  
Create a program that will request a distance in kilometres and output the same distance in miles. 

- 1 mile = 1.60934 kilometres
- 1 kilometre = 0.621371 miles


## 3. Holiday Cost

Sonje has been invited on a holiday by her friends, but she is not sure how much it will cost in total.  
She knows the cost of the hotel will be $75 per night.  
She would like to be able to enter estimates for daily food cost and daily activity cost and then work out the total based on the number of days for the trip.  
For simplicity, assume that each day's costs are the same.  
Help Sonje by writing a program that will figure out the total cost for the holiday.  
Here is some sample output with user entry:

```
Daily food cost: $65.50
Daily activities cost: $49
Number of days: 4

The trip will cost: $758.0
```

## 4. i-stop Calculation (Percentage)

A certain car brand has a feature called **i-stop**, where the car's engine is turned off to increase fuel economy.  
The car's display shows the current percentage of stoppage time that i-stop has been engaged. E.g. this is what the car's display might show:  
```
i-stop ON:       1m 2s
Time Stopped:    2m 41s
Percentage:      38.5%
```

Are you seeing how this works? Looks like our I, P, O pattern...  
Write a program to produce the percentage based on the time on and the time stopped. This should be easy enough for you by now.  
**But wait...**  
It's not so easy dealing with minutes and seconds like in the example. How do we handle that?  
The answer is to develop this program **iteratively** - not trying to solve the whole thing in one go. So...  

For our first version, let's just use total seconds and ignore the minutes+seconds output.  
This will help us focus on the core of the program before we figure out customising the outputs.   
 
- Write a program that asks for the **time on** and the **time stopped** in seconds, then displays the percentage.  
- Use the same example above to test, so 62 seconds on, 161 seconds stopped should give 0.38509... (don't worry about formatting the output neatly)  

When you have that working, you can then focus on enhancing the program.  
Keep the inputs the same, but write the output so it appears as above... How?  

Remember how the **modulo** operation works, and is useful for repeating cycles like time in minutes and seconds?  
We know:  
`161 seconds is 2 minutes and 41 seconds`  
Because:    
`161 // 60 = 2`  
`161 % 60 = 41`  

Also, 0.385 isn't the percentage we want. We want something more like 38.5%. So, what do we need to do to get from 0.385 to 38.5?    
(Don't worry about the number of decimal places at this stage; we'll learn about handling that later using string formatting.)

Knowing this, complete your program so that it outputs like we want. As always, use good variable names.  
Here's a full sample output (with the user inputs 62 and 161 we've been testing with):

```
i-stop on in seconds: 62
Time stopped in seconds: 161

i-stop ON:      1m 2s
Time Stopped:   2m 41s
Percentage:     38.50931677018634%
```

Before you finish with this file, "uncomment" your previous code for all programs.  
Leave the comments for headings, but return the code back to normal.  
To do this, select the lines of code and press `Ctrl+/` for each program.  

# Practice and Extension

These final sections in practicals are not _required_ to be completed for marks, but you will definitely find benefit in completing them for extra practice and to extend yourself.  
The more practice you do, the more you develop and "lock in" your new skills.  

Create a new file, `practice.py` to complete these tasks in:

## BMI
Implement the following algorithm for calculating BMI (body mass index):

```
get height 
get weight
bmi = weight / (height ** 2)
display bmi
```

## Maths Operators
There is a list of common mathematical operators in your notes.   
Write a program that asks the user for two floats called `lhs` and `rhs`, then prints the outputs for the expressions that use those numbers and a maths operator.  
Note that we are OK with a variable name like `lhs` here because: 

- it's a very [common abbreviation for "left hand side"](https://en.wikipedia.org/wiki/Sides_of_an_equation) 
- it is unambiguous in this context
- there is no better, more obvious name (e.g. it doesn't mean `age` or `score` or anything else)

Example, if the user enters 2.5 and 3, it would print:

```
2.5 + 3.0 is 5.5
2.5 * 3.0 is 7.5
2.5 // 3.0 is 0.0
...
```

Use as many operators as you can - not just these ones.

## Number Conversions

Write as many programs as you can handle that convert values in one unit of measurement to another, such as (and the reverse):

- kilograms to pounds
- fahrenheit to celsius
- feet and inches to metres and centimetres
- currencies...

# Extension

If you're cruising and want more of a challenge, look up [how to do string formatting](https://docs.python.org/3/library/stdtypes.html#str.format) so that you can produce neatly lined up output with a fixed number of decimal positions for the above programs, especially the i-stop one.  

## Save your work
If you did your algorithms from earlier in this prac using the computer, you can copy and paste the text into your new PyCharm project.  
PyCharm lets you create text files, so right-click the project folder and choose **New > File** and name this one `questions.txt`  

Note that this is a **text file**, not a Python file (or a Word document or whatever).  
Just put normal (unformatted) text in here and make sure you have simple headings for each question to help you (and us) find the questions that match the answers.   

# Deliverables
This section summarises the expectations for marking in this practical.

questions.txt  with:

- Logic Exercise
- Algorithms
- Problem Decomposition
- Quick Questions - Variables

programs.py with:

- Discount Price
- Miles to Kilometres
- Holiday Cost
- i-stop Calculation (Percentage)


## Submit
Now **submit your work to LearnJCU**.
Remember to include both your `questions.txt` and `programs.py` files.
