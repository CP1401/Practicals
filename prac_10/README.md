# Practical 10 - Files 

**All students (internal and external), please submit your prac work via LearnJCU each week by the due date.**  

Write your answers for the early non-coding questions in a simple text file called `questions.txt`.  


## Quick Questions

1. Explain the difference between the `'r'` and `'w'` modes when opening a file.
2. What is a **file object** and how is it different from a file name or the file's contents? 
3. Why is it necessary to close a file after it has been opened and used?  
4. What is a good principle for deciding whether a literal value should be stored in a CONSTANT?
5. Write a single Python expression that would evaluate to the file extension (e.g. `txt`) of a variable like `filename = "this_is_a_name.txt"` or `filename = "document.docx"`  
6. What is a good number of quick questions to have at the start of a practical?

## Logic Exercise

Consider the following list of 3 statements:  

- There is exactly 1 false statement in this list.
- There are exactly 2 false statements in this list.
- There are exactly 3 false statements in this list.

How many false statements are there in the list; 0, 1, 2 or 3?


# Python Coding - Files

As you do individual work on your computer, if you need help, start by talking to your peers.  
You are encouraged to use Slack to ask questions of others in the class.

## Example
Let's walk through a complete example, from problem description, through problem solving to code and testing.  
Just read along and understand. Do not "do" any of this until asked, just read it and make sure you understand.  
 
### Problem Description:
Geraldine Gamer likes to record her gaming scores, 
so each day she types her best score as a floating-point number into the file "scores.txt".  
She wants to process this file and find out what her average score is.  

### Algorithm

- We need to open the file for _reading_ and close it at the end.  
- We know that each line is the same kind of data so we can process it with a definite loop, doing the same thing per line.  
    We process _each_ line, so that's definite (for loop), not _until_ some condition happens.
- We should know the "accumulation pattern" by now, so the total and average should be easy. 

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

### Code

Note: we don't usually use the variable name `file` because we'd like to know whether it's for 
reading input from (`in_file`) or writing output to (`out_file`).  
These are not world-standard kind of names, but they are more meaningful than `file` or `f`, etc. 
and should help us avoid trying to write output to an input file or vice versa. 
  
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

Notice also that we `close` the file as soon as we've finished with it (not after the average part).

### Testing

Test data for this kind of program is stored in a file.  
Copy this text into a new file (not Python file) called `scores.txt`, saved in the same folder as this prac's program files,   
You can also [download it here](./scores.txt).
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
    Do this now. Note that if the file doesn't exist, the program will crash and that's fine for now...  
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

## 1. Read a String from a File
Create a new text file in your prac_10 directory called `name.txt`.  
Put your own name in the file.
 
Write a simple program that _reads_ this `name.txt` file and greets you, example:
```
Greetings Lindsay!
```

Note that since we want the entire contents of the file in one string, we don't need any kind of loop, 
we can just `read` the file, like:  
```python
in_file = open("name.txt", "r")
text = in_file.read()
```

Did it work?  
If you got something like
```
Greetings Lindsay
!
```
Then what's happened is the `text` variable includes the new line in your file.  
You can solve this problem in two ways.  
- Edit the file so there's no line break
- Strip the new line character (any whitespace from the ends of the line) from text with:
```python
text = in_file.read().strip()
```

## 2. Write Numbers to a File
**Write a complete Python program** that _writes_ a range of numbers to a file.  
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


## 3. Greater-Than Counter
Write a program that _reads_ a file of floating-point numbers, 
and counts how many of those numbers are larger than a user-specified lower limit.  

### Example file:
Copy this text into a new file called `recentrain.txt`,  
or [download it here](./recentrain.txt).
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
Filename: recentrain.txt
Threshold: 10
Processing...
6 out of 10 (60.0%) of values are greater than 10.0.
```


## 4. BMI File
File: `bmi_files.py`

Write a program that writes to and reads from `bmis.txt` (not at the same time).  
Reuse your code from [Prac 6](../prac_06/README.md#example) (and 7) where you calculated a person's BMI based on height and weight.

The first part of your program should ask the user for a number of people, 
then repeatedly ask for the details for that many people. (You did just think of what kind of loop to use, didn't you?)  
For each person, calculate their BMI, but don't print it to the screen... write it to the file "bmis.txt".  
Don't forget to close the file when you have finished.  

Test this and confirm it works as you expect.  

Then, write the second part, which should read the file and display the BMI and weight category similar to how we've done it before:  

```
BMI 23.5, considered normal
BMI 25.5, considered overweight
BMI 24.2, considered normal
BMI 16.3, considered underweight
BMI 32.0, considered obese
```

## 5. File Filter
File: `file_filter.py` 

Write a program that reads a file and "filters" it, writing only certain lines to another file.  
In the lecture, we wrote a program that read [letter.txt](./letter.txt) and printed every line that started with a capital.  

For this program, write a program that asks the user for three things:   
- input file name 
- output file name
- a search string to look for lines that start with

Read the input file, and then for each line that starts with the search string, write those to the output file.

### Interesting Examples:

- This file is a "Markdown" text file. The headings all start with '#'.  
    If the user chose this file and searched for '#', then the output file would contain all of the headings.
- Similarly, HTML headings are `<h1>`, `<h2>` etc. so you could filter/strip those.
- Python comments use `#` or `"""`, so why not try writing getting your program to extract just the comments.
    You would need to `strip()` the lines to account for indenting.    

### Extensions (Optional):

- Get your program to simply search for lines that have the search string _anywhere_
    Lindsay starts a lot of sentences with "So". If you had a [transcript file](./transcript.txt) of one of his lectures and searched for "So", you could make a new file that contained those sentences.  
- Filter in other ways (not based on a user string), like lines that start with numbers or vowels or white space, etc.

### How are you going with the fundamentals?

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
- Write the programs from the "Do this now" in the lecture, including the one that prints only the lines of [letter.txt](./letter.txt) that start with a capital. 

# Extension

## i. Generating A File Of Random Floating-Point Numbers
Write a program that writes a customised collection of random integers to a file.  
Ask the user for the inputs as below, then generate the file.  
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

`questions.txt`  with:

- Quick Questions
- Logic Exercise

`example.py` with updates

Exercises:

- `example.py`
- `programs.py` with exercises 1, 2, 3 
- `bmi_files.py`
- `file_filter.py`