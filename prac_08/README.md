# Practical 08 - Lists

This practical builds on the **Lists lecture** as well as previous practicals.  
If you haven't learned from those, then go back and do so before continuing with this practical work.

Write your answers for the early non-coding questions in a simple text file called `p8questions.txt`.

## Quick Questions

1. What is the main difference between a list and a tuple?
2. What is the convention for naming lists?
3. What would be a good name for a list of cities?
4. How many elements can you store in a list?
5. True or False? Elements in a list must all be of the same type (e.g. all strings or all integers)?
6. What does Python's `len` function do? What types can it be used with?

## Lists Warmup

### Warmup Part 1

Without running any code, write down your answers to these questions in your `p8questions.txt` file (under a "Lists
Warmup" heading).  
Then use the **Python Console** to see if you were correct.  
**Seriously**, do it in your head first; don't just run code to find the answers. You don't learn as much when you do
that.

Consider the following Python list definition:

`numbers = [10, 20, 40, 81]`

**What values do each of the following expressions have?**

    numbers[0]
    numbers[-1]
    numbers[3]
    20 in numbers
    1 in numbers
    numbers[1] + numbers[2]
    len(numbers)

### Warmup Part 2

Again, write your answers in `p8questions.txt`.  
When you've had a go, check your answers in the Python console.

**Write Python statements or expressions to achieve the following:**

1. Change the first element of numbers to 1
2. Change the last element of numbers to 4
3. Check if 1 is an element of numbers
4. Print the second value in the list multiplied by 10

# Python Coding - Lists

## Example

Let's walk through a complete example, from problem description, through problem solving to code and testing.  
Just read along and understand. Do not "do" any of this until asked - just read it and make sure you understand.

### Problem Description:

This is a problem from the lists lecture:
> Julie is planning a holiday and wants to record all the places she goes in the order she visits them.   
> Once she returns, she wants to be able to display the list of places and also which place had the longest name (
> because she likes that sort of thing).

Using our technique of reading the description looking for nouns, verbs, things that might be function, data types, etc.
we should see the plural "places" (as well as "list of places") and recognise the need for a list.

### Algorithm

```
places = empty list
get place
while place is not empty
    add place to places
    get place
for place in places
    print place
```

Note a few things here:

- A good name for a place is... `place`
- A good name for multiple (a list of) places is... `places` - even in pseudocode, use good names. Good names for lists
  are often plurals of the items they contain.
- We have "empty list" as our generic way of specifying an empty list. Different languages will implement this in
  different ways, so we don't want `[]` here. Same for adding a place to the places list.

### Code

```python
places = []
place = input("Place: ")
while place != "":
    places.append(place)
    place = input("Place: ")
print("On my holiday, I went to: ")
for place in places:
    print(place)
```

Again, see how similar to pseudocode it is, but now we use things like `[]` and `append`.  
This doesn't implement the "longest" part of the problem... that's coming later.

### Testing

Create a new Python file, `p8example.py`.  
**Now, you type or copy this example code and test it** with a few places. Is it OK?

When testing while loops, a good idea is to test what happens if they are False the first time (so the body never
executes).  
Test this with an empty place to start with (just press enter).

### Things to do

Remember to do these one at a time and test each one.

- Let's assume that all place names need to be stored in title case (e.g. "New Zealand" not "new zeaLAND").  
  Use Python's `.title()` string method to do this.  
  Consider the **DRY** principle. We only need to title the names we keep when we append.  
  (In Prac 3 we learned to use `.upper()` and `.lower()`, now we're using another useful string method.  
  Watch what happens after you type the `.` and you'll see all the other methods available!)

- Now let's try finding and displaying the longest name.  
  We'll need to keep track of the `longest_place`, so create a variable for this and initialise it to the empty
  string, "".  
  Now what do we do? Well, each time we see a place, we can compare the length of its name to the length of the
  longest_place.   
  We already have a loop to get the places and a loop to display them, so we **do not** need a third loop. We can use
  either one, but let's pick the for loop.  
  Each time through the loop, compare the lengths and update the `longest_place` when you find a new longest place.  
  Remember that every time (literally every time) you think of using a decision structure (like this), you should
  consider which of the patterns applies. So, which pattern applies here? At the end of the loop, print the longest
  name.

### Output

Example. Remember that user input does not need to be re-output. It's user input, not something you print in your
program.  
We've copied from the PyCharm Run window when the program was finished, so here we have program output and input
together.

```
Place: new zealand
Place: That nice little spot by the sea
Place: OLD zealand
Place: 
On my holiday, I went to: 
New Zealand
That Nice Little Spot By The Sea
Old Zealand
The place with the longest name was That Nice Little Spot By The Sea
``` 

Got it?  
When you have, test it again with an empty first place. You should see:

```
Place: 
On my holiday, I went to: 
The place with the longest name was 
```

This doesn't quite seem right...  
**Change it** so that `if` the list is empty, the program runs like:

```
Place: 
I went nowhere :(
```

Did you think about which decision structure pattern applies here?

Test this, and do "regression testing", where you not only test the new path you added (empty list), but you also test
the normal execution to ensure you didn't break anything.

# Coding Exercises

## 1. Random numbers

File: `random_numbers.py`

(Quick note: NEVER name your files the same as a Python module. If you call this file `random.py` it won't let you
import the real random.)

(Another quick note: Don't let yourself get **stuck** on something for too long. If one part of one question starts
taking you too long, just leave it, move on and come back to it later.)

**Write a complete Python program** that ask the user for quantity of random numbers and a maximum, then generates and
store that many numbers between 0 and the maximum. When you've got this part working, add the following interesting
additions:

- minimum
- maximum
- random choice from existing list (Hint: if there are 7 numbers it will be a number at a random index 0-6)
- the list reversed*
- the list sorted*

*Note**: Python's `.reverse()` and `.sort()` list methods do NOT **return** the reversed or sorted list... they modify
the list in place.  
So, if you write something like:

```python
print(numbers.sort())
```

You will not get what you expect. You'll sort the list, but the method will return `None`, which is what you'll see
printed.  
You need to do this in two steps - or discover new functions that we haven't explicitly taught you :).

### Sample Output

```
How many random numbers: 7
Maximum number: 100
The numbers are: [0, 26, 27, 23, 83, 35, 91]
The minimum is 0
The maximum is 91
A randomly chosen number is 91
The numbers reversed are [91, 35, 83, 23, 27, 26, 0]
The numbers sorted are [0, 23, 26, 27, 35, 83, 91]
```

## 2. Test Scores

File: `test_scores.py`

**Write pseudocode** for the `main()` part of a program that asks the user to enter 4 test scores between 0 and 100,
then displays a JCU grade for each score and also the average test score.

When you have written the pseudocode for main, implement your solution in Python code and test it with a range of
meaningful data.

Remember that we've done the [JCU grades](../prac_06/README.md#3-jcu-grades) question before, so copy your function from
that practical code file.

### Sample Output

```
Score: 3
Score: 50.5
Score: 66
Score: 100
Score 3.0, which is F
Score 50.5, which is P
Score 66.0, which is C
Score 100.0, which is HD
The average score was 54.875
```

### Enhancements

When you have that working...

- We asked for `4` scores. Have a look at your code... did you use `4` as a numeric literal or a constant?  
  Change 4 to 3... Did you have to change the program in more than one place?  
  If so, then you've
  missed [one of the things we've taught](https://github.com/CP1404/Starter/wiki/Programming-Patterns#constants)...  
  As a **strong guideline**: if you need to use the same literal more than once, you should turn it into a **constant**
  .  
  Do this now if you haven't already.

- Add error-checking to the test score inputs to ensure they are between 0 and 100.  
  You should be getting good at this by now :)
  but do notice that it's easy to do this kind of "iterative development" where you don't try and get it working all at
  once. Error-checking is a common feature to add _after_ you have the core functionality working.

- Add a feature that shows the user what the **trend** is.  
  If the last score in the list is higher than the average, then the trend is "positive", otherwise it's "not positive".

- Upgrade your print outputs so the output is formatted nicely like:

```
Score 1: 3
Score 2: 50.5
Score 3: 66
Score 4: 100
Score 1 was   3.0, which is N
Score 2 was  50.5, which is P
Score 3 was  66.0, which is C
Score 4 was 100.0, which is HD
The average score was 54.875
The trend is positive
```

## 3. Debugging Lists

File: `debugging.py`

Similar to the previous practical's debugging exercises:

- Copy the code from [debugging.py](./debugging.py)
- Run the code and see what problems you can find.
- Complete the template in this file, adding comments to explain the **problems** (bugs) you find.
- **Remember**: debugging is about finding bugs, not just generally improving code. We're not interested in formatting
  and style here, just functionality.
- Then, comment-out the broken code and include fixed code in the provided section.

## 4. Extract data

File: `extract_data.py`

Often, we get list data that is not homogenous, so not a list of names or countries, etc. but a list that's like a
database 'record' (row) where each 'field' (column) represents a different kind of value.  
We can extract this data using indexing.

Consider and copy the following code:

```python
record = ["Jimmy", "Smith", (8, 12, 1928), "piano"]
```

Write code to extract and print specific data, like in this sample output:

```
Last name: Smith
Born: (8, 12, 1928)
Jimmy was born in 1928 and was a great piano player.
```

As ALWAYS, do this one step at a time. You don't want to write the whole thing before getting just the first line to
work.

Test your code with different data like below. Do this by commenting out your existing data for Jimmy Smith and paste
this one below it:

```python
record = ["Wes", "Montgomery", (6, 3, 1923), "guitar"]
```

# Practice and Extension

These final sections in practicals are not _required_ to be completed for marks, but you will definitely find benefit in
completing them for extra practice and to extend yourself.  
The more practice you do, the more you develop and "lock in" your new skills.

Create a new file, `practice.py` to complete these tasks in:

## A. More Numbers

Add extra cool things to your `random_numbers.py` program:

- The total
- The average
- All of the numbers over half of the maximum
- A new list containing the squares of the numbers
- A new list containing the humbers halved
- etc.

## B. BMIs

Rewrite your bmi program from the previous prac (with the file in this prac's folder) so that each time you ask for a
user's details, you store their BMI in a list.  
Then display all of the BMIs along with their weight category.

# Extension

## i. Game Scheduler

The **League of Extraordinary Jazzers** have decided to have some jazz-offs for a new worldwide webTV special intended
to revitalise interest in... jazz fights.  
So, we need a program to schedule the jazz-off fights between two teams of possibly-deceased jazz greats.  
In between practising his octave-laden smooth soloing, Wes knocked up a piece of code to try and schedule the
competition, but it's not quite right...

```python
red_team = ["Miles", "Ella", "Chet"]
blue_team = ["Louis", "Wes", "Jimmy"]
for player in red_team:
    for opponent in blue_team:
        print(f"{player} vs. {opponent}")
    print("---------------------")
print()
```

Produces output:

```
Miles vs. Louis
Miles vs. Wes
Miles vs. Jimmy
---------------------
Ella vs. Louis
Ella vs. Wes
Ella vs. Jimmy
---------------------
Chet vs. Louis
Chet vs. Wes
Chet vs. Jimmy
---------------------
```

Not too bad, but we want it organised by round.   
Miles plays Louis in round 1, then Wes in round 2...  
So, the goal output is:

```
-------Round 0-------
Miles vs. Louis
Ella vs. Wes
Chet vs. Jimmy
-------Round 1-------
Miles vs. Wes
Ella vs. Jimmy
Chet vs. Louis
-------Round 2-------
Miles vs. Jimmy
Ella vs. Louis
Chet vs. Wes
```

Have a go at writing new code to schedule this killer competition!  
Hint: this is probably best done with indexes not elements. Start by trying to get the indexes right, then use them to
access the names. So, aim for:

```
-------Round 0-------
0 vs. 0
1 vs. 1
2 vs. 2
-------Round 1-------
0 vs. 1
1 vs. 2
2 vs. 0
-------Round 2-------
0 vs. 2
1 vs. 0
2 vs. 1
```

Note also: this should work for two teams of equal size with any number of players (not just 3).

## ii. Multiple Records

Enhance your `extract_data.py` program. Leave your original code intact and do this below it in the same file.

First, just extract the year, so you see:

```
Jimmy was born in 1928 and was a great piano player.
```

Notice that "Piano" is now more appropriately "piano" since it's used in a sentence here.

Then (extension alert!), create a list of lists where each inner list is a record like this.  
We'll do this more in Programming 2 so don't worry if this is a stretch too far.

Your program should display a line like the above for each of the great jazz musicians in your list.

# Deliverables

This section summarises the expectations for this practical.  
Please follow the [submission guidelines](../README.md#submission) to ensure you receive marks for your work.

**Files required:**

`p8questions.txt`  with:

- Quick Questions
- Lists Warmup - parts 1 and 2

`p8example.py` with updates

Exercises, each in their own file:

- `random_numbers.py`
- `test_scores.py` (with pseudocode)
- `debugging.py`
- `extract_data.py`