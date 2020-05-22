# Practical 10 - Files 

**All students (internal and external), please submit your prac work via LearnJCU each week by the due date for your situation.**  

Write your answers for the early non-coding questions in a simple text file called `questions.txt`.  


## Quick Questions

1. Explain the difference between the 'r' and 'w' modes when opening a file.
2. Why is it necessary to close a file after it has been opened and used?  
3. 
4. 
5. 
6. 

## Logic Exercise

Consider the following list of 3 statements:  

- There is exactly 1 false statement in this list.
- There are exactly 2 false statements in this list.
- There are exactly 3 false statements in this list.

How many false statements are there in the list; 0, 1, 2 or 3?


# Python Coding - Files

As you do individual work on your computer, if you need help, start by talking to your peers.  
External students are encouraged to use Slack to ask questions of others in the class (but you don't need to post your answers there).

## Example
Let's walk through a complete example, from problem description, through problem solving to code and testing.  
Just read along and understand. Do not "do" any of this, just read it and make sure you understand.  
 
### Problem Description:
Geraldine Gamer likes to record her gaming scores, 
so each day she types her best score as a floating-point number into the file "scores.txt".  
She wants to process this file and find out what her average score is.  

### Algorithm

```
total = 0.0
count = 0
open "scores.txt" for reading as in_file
for line in in_file
    score = line as float
    total = total + score
    count = count + 1
close in_file
average = total / count
print average
```

Notice that we choose to use a for loop (definite iteration), because:

- We know how many times we want to run the loop - once for each line in the file
- We will do the same thing with each line


### Code

```python
total = 0.0
count = 0
in_file = open("scores.txt", 'r')
for line in in_file:
    score = float(line)
    total += score
    count += 1
in_file.close()
average = total / count
print(f"Average = {average:.1f}")
```

### Testing

Test data for this kind of program is stored in a file.  
Copy this text into a new file (not Python file) called "scores.txt", saved in the same folder as this prac's program files,   
You can also [download it here](./scores.txt), remembering to click *Raw* before copying.
```
56.8
34.0
45.5
49.3
```

Output
```
Average = 46.4
```

### Things to do

Create a new Python file, `example.py` (File > New > Python File)    
**Now, you type this code in (don't copy it)**, and **test it** to see you got the expected output.  
The reason you want to _type_ instead of _copy_ this code is because it helps you learn to use the IDE (e.g. use autocomplete!), 
type code accurately, and develop an eye for detail.

- The filename in the program is a literal, but we can easily make it a variable and ask the user for the file name.  
    Do this now. Note that if the file doesn't exist, the program will crash and that's fine for now.  
    We'll learn how to handle exceptions in Programming 2. 
    Test it with a different file (maybe the [recentrain.txt](./recentrain.txt) file from below).

- Currently, the program just prints the final average.  
    Make it print a running total, so output would look like: 
```
Score = 56.8   Total so far =   56.8
Score = 34.0   Total so far =   90.8
Score = 45.5   Total so far =  136.3
Score = 49.3   Total so far =  185.6
Average = 46.4
```

If you're not sure how to do the lining up using string formatting, you can check the [example.py file here](./example.py).


# Coding Exercises
 
(Unless otherwise specified) Write all of your answers to the following questions in a single Python file called `programs.py`  
At the top of each program, put a **comment** (starts with a `#`) with the exercise number/name (copy-and-paste it from here) so you/we know what the program is for later.  
Example:

```python
# 2. Miles to Kilometres
number_of_miles = int(input("Miles: "))
...
``` 

## 1. Writing Numbers To A File
**Write a complete Python program** that writes a range of numbers to a file.  
Here is the algorithm partly done for you in pseudocode:
```
open file "range.txt" for writing as out_file
for number in range ? to ? in steps of ?
    write number to out_file
close out_file
```

It is up to you what range to generate.  
Try these, and some of your own ideas:

- all the odd numbers from 0 to 99
- 0 to 100 in 10's
- 20, 19, 18... 0

Run your program each time with different ranges - commenting out the range line when you make a new one (so you keep the old one).  
You should write each number to a new line.


## 2. Greater-Than Counter
Write a program that reads a file of floating-point numbers, 
and counts how many of those numbers are larger than a user-specified lower limit.  

### Example file:
Copy this text into a new file called "recentrain.txt",  
or [download it here](./recentrain.txt) remembering to click *Raw* before copying.
```
12.4
10.0
10.1
0
8.4
13.9
19.1
141.0
33.5
1.2
```

### Example output: 

```
Enter filename: recentrain.txt
Enter lower limit: 10
Processing...
6 out of 10 (60.0%) of values are greater than 10.0.
```


## 3. BMI File
File: `bmifiles.py`

Write a program that writes and reads from "bmis.txt" (not at the same time).  
Reuse your code from [Prac 6](../prac_06/README.md#example) (and 7) where you calculated a person's BMI based on height and weight.

The first part of your program should ask the user for a number of people, 
then repeatedly ask for the details for that many people. (You did just think of what kind of loop to use, didn't you?)  
For each person, calculate their BMI, but don't print it to the screen... write it to the file "bmis.txt".  
Don't forget to close the file when you have finished.  

Test this and confirm it works as you expect.  

Then, write the second part, which should read the file and display the BMI and weight category similarly to how we've done it before:  

```
BMI 23.5, considered normal
BMI 25.5, considered overweight
BMI 24.2, considered normal
BMI 16.3, considered underweight
BMI 32.0, considered obese
```

In *all* of your programs by now, you should have clear ideas about the fundamental principles we've learned, so (example):  

- You know if you have to refer to the filename (literal) more than once, then it should be a... CONSTANT,
- You know SRP... your functions should not (usually) print, when they should return... so you can reuse the exact same function from prac 6 for this program,
- You know your names must be meaningful,
- You know you use definite iteration (for loop) for things like a fixed number of times,
- You know every time you open a file, you should close it as soon as you're finished,
- You know programming is fun...


# Practice and Extension

These final sections in practicals are not _required_ to be completed for marks, but you will definitely find benefit in completing them for extra practice and to extend yourself.  
The more practice you do, the more you develop and "lock in" your new skills.  

Create a new file, `practice.py` to complete these tasks in:

- Write a program that asks the user for a filename, opens that file and then simply prints how many lines are in the file.
- Write a program that asks the user for a filename, opens that file and then simply prints the number of characters in the file.
- Write a program that asks the user for a phrase and a filename, opens that file and then searches the file for the phrase, printing either "Found" or "Not found".


# Extension

## i. Generating A File Of Random Floating-Point Numbers
Write a program that writes a customised collection of random integers to a file.  
Ask the user for the 4 values below, then generate the file. 
So,
```
Enter the filename: RandomNumbers.txt
Enter the minimum integer: 12
Enter the maximum integer: 50
Enter the number of random integers to generate: 9
```
would produce, RandomNumbers.txt containing something (random) like: 

```
22
45
41
19
31
23
40
28
20
```

## ii. Simple File Statistics
Given a file with a floating-point number on each line, write a program that will calculate:

a.	the total
b.	the average (arithmetic mean)
c.	the minimum
d.	the maximum
e.	the median (harder - you will need to use a list)


# Deliverables
This section summarises the expectations for marking in this practical.

questions.txt  with:

- Quick Questions
- Logic Exercise

Exercises:

- example.py
- programs.py with each exercise 
- bmifiles.py