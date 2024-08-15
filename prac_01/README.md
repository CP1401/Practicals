# Practical 01 - Problem Solving and Algorithms

**Welcome to practicals!**

If you haven't read the introduction to pracs and marking, please [read this now](../README.md).  
**Please submit your prac work via LearnJCU each week by the due date according to
the [submission requirements](../README.md#submission).**

## Community

It's a good idea to start getting to know your IT@JCU community a bit more...

In lecture 1, we established that it was **not OK** to work together with others on your assignments for this subject,
including these simple rules:

- Never give someone a copy of your work
- Never get a copy of someone else’s work
- This includes looking at theirs or having someone look at yours

You have to do your own work in order to achieve the learning outcomes.  
However, it's still really helpful and good practice to work with others to understand problems and to discuss
solutions.  
You **are allowed** to talk with others about these things... you just can't go too far.  
Communication is a big part of IT, and it helps to know a little about who you are communicating with.

**Internal students:**

If you're in a face-to-face practical class with other students, you will play the "name game" as directed by your
tutor (your name and what you like that starts with the same first letter, e.g., "I'm Yasmin and I like yachting").

**External students:**

**Introduce yourself in Slack** - include where you are studying from and any other interesting details you're happy to
share. Thanks!

Great, now let's get ready to focus on problem solving...

Record your answers for each of the below questions in a simple text file, `questions.txt`. You can use PyCharm (if you
already know how), Notepad or any suitable program for creating your work file.

## Logic Exercise

Sometimes in our learning, we will have non-IT-based exercises to help us with problem solving in any context. The
emphasis is on developing skills that will help you approach new problems and work towards solutions.   
These will not be silly trick riddles, but puzzles with logical, deducible answers.   
The goal is **"to reach a conclusion by reasoning"**.  
One of the important factors in attempting these questions is to really analyse the question and the information given (
or not given) in the question without making inappropriate assumptions. This is a valuable skill in IT and programming.

If you are ever working in a group on these, and you already know the answer (or you figure it out quickly), please help
the others in the group by NOT just saying the answer. Maybe give appropriate guidance if needed so that others can work
it out themselves and learn through the process.

**Here's our first one...**

- Brown, Jones and Smith are three friends.
- One of them is a project manager, one is a consultant, and the other is a programmer.
- The programmer, who is an only child, earns the least money.
- Smith, who married Brown\'s sister, earns more than the consultant.

**What is each person's job?**

Note: record your answer for this question in your `questions.txt` file under the heading "Logic Exercise", so it's
clear.

## Algorithms

Record your answers to the following questions in your text file called `questions.txt`. Use a heading for each one.

The following exercises are focused on the logic of algorithms, rather than the exact pseudocode.  
We're not going to write computer programs for these, so we are just focused on the basics of writing a set of
understandable instructions.

### Example

Here's an example of an algorithm (written in simple pseudocode) to determine if it's safe to go out and play based on
the sun (uv index):

```
get uv index
if uv index < 5
    go out and play
else
    do not go out and play
```

Notice the first line...  
We can't just say: `if uv index < 5` without knowing what `uv index` is, so we have to **get** it first.

### Algorithm with I, P, O

**Write an algorithm** to calculate the brew ratio of coffee, given the dose (quantity of coffee beans in grams) and the
yield (brewed coffee in grams).  
Example: A dose of 18g and yield of 45g is a 1 to 2.5 brew ratio.

This algorithm doesn't have any control structures, but just uses **input, processing and output**.  
In our lecture, we saw a similar example for calculating the volume of a box:

```
get length, width, depth
volume = length * width * depth
print volume
```

Notice that we used a "variable" (more on this later) to store the volume so that we could refer to it when printing the
result.

### Algorithm with Decision

**Write an algorithm** to determine if you can afford to buy an item based on its price and the money you have in your
pocket.

Notice how similar this question is to the UV index example above. Your pseudocode should be structurally like the example.  
This algorithm should have included the **decision** (or selection) control structure. We will learn more about that
soon.

### Algorithm with Repetition

**Write an algorithm** to instruct a teenager how to clean their room. They have lots of things on the floor, and need
to pick them up until there are no more things on the floor.

Note: we are not trying to write code here, so just include simple instructions like you might say to a person or
robotic assistant.  
This algorithm should have included the **repetition** (or iteration or loop) control structure. We will learn more
about that later, but for now, you can consider using words like `while` and `repeat`.  
Here's a simple example for eating food:

```
eat mouthful
while still hungry
    eat mouthful
do the dishes
```

Notice how the repeated section is indented. We keep doing this "while still hungry" (or "until not hungry").  
Notice how the last line is not indented. We know we only do the dishes when we've finished eating (repeating).

## Problem Decomposition

For the following problem descriptions, identify the **nouns** and **verbs** (separately) in each.

Note: You will end up with 4 separate answers for this section - the nouns & verbs, then the algorithm, for each of the problems.

Write two separate lists (with subheadings) for each.  
(Don't get hung up on the exact details of the words.)

Then go through the set of nouns and verbs and work out which ones are irrelevant or duplicated and remove them from the
lists.

See if what's remaining is what you need to know to write an algorithm.  

Nouns = variables to store  
Verbs = actions to do  

1. Happy Photos needs a way to calculate the total charge for a customer's booking. The system will use the customer's
   name and the date of the booking to make a unique booking id. The hourly charge, and number of hours will be entered,
   and the total charge and id code will be displayed.

2. A road trip planning system will ask the user for the distance travelled (in km) and the travel time in minutes. The
   user will then be shown the average speed (in km/hour) over the trip.


**Write algorithms for each of these problems using pseudocode**.  
At this stage, we're not worried about getting the details 'perfect', we just want to get used to problem solving
processes.

As you do this, think about what **assumptions** you're making.  
Good assumptions are an important part of IT and problem solving.

Potentially, you found it easier to write the algorithms after the "decomposition" step.  
As problems get bigger, we need to be more systematic about our methods.

## Python and PyCharm

(Individual work now. This section does not need to be submitted.)

We are not going to write any substantial programs in this prac, but we are going to run PyCharm and see how it works.

If you have your own computer, you
can [follow these instructions to install Python 3 and PyCharm Professional](https://github.com/CP1404/Starter/wiki/Software-Setup)
remembering you only need Python and PyCharm.

Let's start by getting used to working with the PyCharm IDE (Integrated Development Environment).  
Note: Your screens may look different than our images or descriptions below depending on versions used.

1. Run PyCharm.  
   When PyCharm first starts you should have a window with a link to create a new project.

    - A PyCharm **project** is a folder on the computer that contains Python source code files and related resource
      files to make your program run... but it's more than that. Always do your coding in files that are part of a
      meaningful project.

    - the **Quick Start** window lists several useful tasks like creating a new project or adjusting the configuration
      of PyCharm

2. Click on **Create New Project**. and choose **Pure Python**. PyCharm asks you where to store your new project and to
   choose an interpreter. Your screen may look different than our image below, but name your new project (folder) for
   your **cp1401practicals**.

    - the **location** can be changed to any place you have access to. Use a folder that you will be able to find later

    - use the **... button** ("meatball menu") to select the location

    - the **interpreter** is the version of Python we need to run our code on the computer.  
      Use the *previously configured interpreter* for Python 3.  
      **DO NOT use a virtual environment (Virtualenv).** They're cool, but we don't need them in this subject... they
      make things harder for you.

   ![New project window - choose previously configured interpreter](../images/Python-Windows-Install-3-Project-1.png)

    - Click the ... menu button to choose a new interpreter and select the System Interpreter you installed earlier.  
      (This is why it's useful to install Python in a directory you can find.)
      Select the System Interpreter you have installed (not a Virtualenv).

   ![Select system interpreter](../images/Python-Windows-Install-4-Project-2.png)


3. Next, let's add our first source code file to the project.  
   **Right-click** on the project name and select  
   **New > Python File**  
   ![New file](../images/01image2.png)

4. This opens a window where you can define the name of the file - call it **hello.py** and hit the **OK** button.
   Always give your files descriptive names so they're easy to find again.

5. PyCharm created a new source code file in the project folder and opened the editor window:
   ![Editor window](../images/01image3.png)

6. Let's learn our first shortcut! Press **Shift+Enter** to add a blank line below the one you're on (no matter where
   the cursor is). Nice!
   Now type the famous line:

   ```python
   print('Hello world')
   ```

7. To **run** this first program, **right-click** in the code editor window and select **run**.  
   (If it didn't work, please check for what the problem might be, and ask the nearest person for help if you need.)

### Project Structure: Use one project for all practicals

PyCharm doesn't just work with individual code files, but with *projects*. You now have a project for your practicals,
and this is the only one you'll need for all pracs.  
So in order to keep your work organised, you will have one well-named folder (directory) for each prac, with well-named
files inside the relevant folder.

Let's get used to following best practice (remember that's one of our goals), and create the first folder...

Right-click on the project name in the top left and select **New > Directory**  
Name this folder/directory

```
prac_01
``` 

This conforms with Python module/package naming conventions, using underscore_lowercase (no spaces).   
Also, by naming it `01` instead of just `1`, when we get to `prac_10`, our alphanumeric sorting will work as we expect (
otherwise, prac2 comes _after_ prac10).

Now that you have the folder, drag your **hello.py** file into it.

**Do not** create new projects for each separate practical.

**Do** use separate projects for each assignment and any other side 'projects'.

### Example program

For fun, let's now copy all of the code from
our [catering calculator example program](https://raw.githubusercontent.com/CP1401/subject/master/cateringcalculator.py)
(Use Ctrl+click to open links in new tabs)  
and paste that into a **new Python file** with the same name, `cateringcalculator.py`.

**Run it**... play with it, change it, break it, see what happens...  
(Don't worry if you don't understand it yet, we've still got a long way to go.)

## Save your work

If you did your algorithms from earlier in this prac using the computer, you can copy and paste the text into your new
PyCharm project.  
PyCharm lets you create text files, so right-click the project folder and choose **New > File** and name this
one `questions.txt`

Note that this is a **text file**, not a Python file (or a Word document or whatever).  
Just put normal (unformatted) text in here and make sure you have simple headings for each question to help you (and us)
find the questions that match the answers.

If you are using a JCU computer, not your own, please **copy your work** (the whole project directory) onto your
portable/cloud storage so you can access it again in the future.  
_Keep every file you ever write in this subject._

# Deliverables

This section summarises the expectations for marking in this practical.  
Please follow the [submission guidelines](../README.md#submission) to ensure you receive marks for your work.

For the first week, we're flexible with how you record your work.  
Ideally, upload your answers in a text file called `questions.txt`.  
But for this week only, we'll accept anything that works for you: photos of hand-written work on paper, Word documents,
text files... whatever you did.

**Files required:**

`questions.txt` (or similar) with:

- Logic Exercise
- Algorithms (IPO, Decision, Repetition)
- Problem Decomposition (3 problems, each with word types and algorithms)

Now **submit your work to LearnJCU** (click on the practical link inside the relevant weekly folder).
