# Practical 02 - Input, Processing and Output 

**All students (internal and external), please submit your prac work via LearnJCU each week by the due date.**  

## Read and Understand
Make sure you read the instructions carefully.  
Do not make the easy bits hard by not reading the instructions.  
We want the challenge to be in the new things you're learning and trying, not in the reading and paying attention to what the questions ask.  
Don't waste time by trying to save time skim-reading. Just read... and understand... then do.  

As you do the early non-coding questions, you can write your answers in a simple text file (`questions.txt`).  
Use whatever text editor you can get to the fastest so you don't waste any time before starting.

# Collaboration 
External students can do the group activities individually.   
Internal students, **form a group of 2 or 3** to do the next two sections (until we get to the programming parts when you can work individually but help each other out if needed).  
Try and remember your new friends' names and use them when you can to help reinforce them in your memory. What do they like that starts with the first letter of their name?   

## Quick Questions

1.	Write two variable names that would be valid and well-named.
2.	Write two variable names that would be valid but not well-named.
3.	Write two variable names that would not be valid.
4.	What is the naming convention for variables in Python?
5.	What is a constant? Give an example of when you would use one.
6.	What is the naming convention for constants?

## Logic Exercise
A drawer contains 10 black and 10 white socks that are all mixed up.
What is the fewest number of socks you can take from the drawer _without looking_ 
and be sure to get a pair of the same colour?

When you've decided on an answer for this, discuss it with a group near you.  
If you have a different answer, try and figure out why/how you arrived at different answers.  
Is there a meaningful way that you can explain your answer, perhaps a diagram that would help?  

As you do individual work on your computer, if you need help, start by talking to your peers.  
External students are encouraged to use Slack to ask questions of others in the class (but you don't need to post your answers there).

To use PyCharm as your text editor:

- Run PyCharm 
- Open your existing Practicals project (made last prac), or if you don't have it with you for some reason, create a new one following the instructions in the last prac.
- Create a new folder (directory) for `prac_02` (remember not to use spaces, and do not make a new project per prac, only new folders).
- Now create a new text file: Choose **File > New... > File**  (not Python file)  
- Name your file `questions.txt` (the `.txt` extension means PyCharm won't try and correct your Python code... it's just text)
- Make sure your new file is inside the prac_02 folder. If it isn't, just drag it in.  


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

- get height 
- get weight
- bmi = weight / (height ** 2)
- display bmi

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

## Extension

If you're cruising and want more of a challenge, look up [how to do string formatting](https://docs.python.org/3/library/stdtypes.html#str.format) so that you can produce neatly lined up output with a fixed number of decimal positions for the above programs, especially the i-stop one.  

# Deliverables
This section summarises the expectations for marking in this practical.

questions.txt  with:

- Quick Questions
- Logic Exercise

programs.py with:

- Discount Price
- Miles to Kilometres
- Holiday Cost
- i-stop Calculation (Percentage)
