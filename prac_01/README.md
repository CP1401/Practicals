# Practical 01 - Problem solving and algorithms 

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

## Save your work
If you did your algorithms from earlier in this prac using the computer, you can copy and paste the text into your new PyCharm project.  
PyCharm lets you create text files, so right-click the project folder and choose **New > File** and name this one `questions.txt`  

Note that this is a **text file**, not a Python file (or a Word document or whatever).  
Just put normal (unformatted) text in here and make sure you have simple headings for each question to help you (and us) find the questions that match the answers.   

If you are using a JCU computer, not your own, please **copy your work** (the whole project directory) onto your portable/cloud storage so you can access it again in the future.  
_Keep every file you ever write in this subject._

## Submit
Now **submit your work to LearnJCU**.
For the first week, we're flexible with how you record your work.  
Ideally, upload your answers in a text file called `questions.txt`.  
But for this week only, we'll accept anything that works for you: photos of hand written work on paper, Word documents, text files... whatever you did.  
