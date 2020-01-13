## Beginner Workshop
Python is a popular programming language and one that we use at Made.com for our back-office computer software. In this 
workshop we will be looking at the basics of Python and programming including; variables, functions and loops. It is 
based on [Chapter 1 - Python Basics](https://automatetheboringstuff.com/2e/chapter1) from the 'Automate The Boring 
Stuff' online course.

As an example of what you could achieve with Python after some study and understanding, see the example programs in 
the [/intermediate](/intermediate) workshop. These include the program [weather.py](/intermediate/task_1/weather.py) 
which will print today's temperature from BBC Weather, [lucky.py](/intermediate/task_2/lucky.py) which given a search 
term, will open the first 5 results in Google for you and [sofa.py](/intermediate/task_3/sofa.py) which will login to 
your Made.com account and buy a sofa. My favourite of example of how we can use programming to automate everyday life is
a program that I've written called [lottery.py](/intermediate/demos/lottery.py) which will automatically login and enter
you in for the lottery for the Harry Potter and the Cursed Child theatre show!

### Before we can start
Make sure you have the Python programming language installed on your computer.
- You can check this by opening the Terminal on Mac or Command Prompt on Windows and typing `python --version` then 
hitting enter. 

```
$ python --version
Python 3.8.0
```

The version number can be different, but as long as you don't see something like the error below, you're good to go.

```
$ python --version
-bash: python: command not found
```

- If you do see this kind of error, then Python is not installed on your computer, and you can use the instructions in 
[Chapter 0 - Introduction](https://automatetheboringstuff.com/2e/chapter0/) to install it.

Pick a piece of software to write Python programs.
- To start with we will be using the the Python Interpreter to write and run small pieces of Python code, but to write
larger programs we will use software called an Editor. This is mostly just a program to write Python code, but it has
other uses such as highlighting when we've written invalid Python code. The program that I use and recommend is 
[PyCharm Community](https://www.jetbrains.com/pycharm/download), but you are of course free to use any other as they all
do the same thing.

### Python Interpreter
So let's write our first Python program! And we'll do this using the Python Interpreter. This is a piece of software 
that will let you write and run Python instructions one line at a time (not great for writing long programs, but great 
for testing or learning). You can start the Interpreter by going to the Terminal/Command Prompt, typing `python` and
then clicking Enter - you should see something like the below. Your cursor will start after the 3 chevrons/arrows, and
this is where we can write Python commands.

```
$ python
Python 3.8.0 (v3.8.0:fa919fdf25, Oct 14 2019, 10:23:27) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> 
```

In programming, the first line of code we typically write and run prints out the text "Hello, World!" - it's somewhat a 
tradition and checks that you can run some basic code. So let's start with that shall we?!

```
$ python
Python 3.8.0 (v3.8.0:fa919fdf25, Oct 14 2019, 10:24:53) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> print("Hello, World!")
Hello, World!
```

Great job! If you can see the same output as above you did it! But what did you do? Let's break it down. `print()` is
the first function you will have used. A function is a block of code that is given a name. Writing the name of function
with brackets `()` will then mean that you would like to run this block of code.

Then inside of the brackets you wrote some text inside of speech marks `"Hello, World!"`. This is the text (called a 
string in programming) that we wanted to output to the screen. And that's it! If that doesn't make sense, good, keep
reading and hopefully it will start to. If it does make sense, even better, but no one likes a show off.

Next lets try playing with some numbers. In Maths we "evaluate" an expression by performing a series of actions with 
numbers. We can use Python to do this for us by using the format below - try it out, and play around with other things. 
You can use [Table 1-1](https://automatetheboringstuff.com/2e/chapter1#calibre_link-1652) for more explanation.

```
$ python
Python 3.8.0 (v3.8.0:fa919fdf25, Oct 14 2019, 10:26:14) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> 2 + 2
4
>>> 2 * 2
4
>>> 2 / 2
1.0
>>> 2 - 2
0
```

### Task 1 - 

### Lesson 1 - Controlling Code
Knowing how to read the flow of code, and control it yourself, is vital in programming. Some computer programs can be 
read top to bottom, others are distributed between multiple files and groups of code lines. This lesson should help you
in starting to understand these concepts and techniques.

Again, read through the 2 chapters below and try out the examples. If you come across errors, double check the code you
have written, ask someone else to check it looks correct or break the problem down line by line, to ensure everything 
you think is there, is. 

[Chapter 2](https://automatetheboringstuff.com/chapter2/) - Controlling the flow of programs (booleans, comparison 
operators, conditions, if statements, while loops, for loops, importing modules)

[Chapter 3](https://automatetheboringstuff.com/chapter3/) - What are functions, global and local scope and exception 
handling 

### Lesson 2 - Data Structures
Lesson #2! You're half way through the Beginner level lessons for this course, well done!! Today we will be looking at
what programmers call "data structures" which is a posh way of saying "data grouped together in a particular way". 

This will include `lists` which are values that contains other values in a particular order, such as a list of integers 
i.e. `[1, 3, 5, 7]`. We also have `tuples` which are similar to lists, but their subtle differences will be explained.
Last but not least, dictionaries, again a collection of values but with more useful ways of identifying data within them
using "keys". Read on dear colleague, and all will be revealed...

[Chapter 4](https://automatetheboringstuff.com/chapter4/) - The list and tuple data types and methods

[Chapter 5](https://automatetheboringstuff.com/chapter5/) - The dictionary data type and structuring data with them

### Lesson 3 - Strings
In programming we refer to text values as "strings", this is because in dawn of programming, this term was used to
describe a series of numbers or words, a "string of 1s". Moving on, text is extremely useful as input and output in
computer programs, so let's see how Python can let us play with strings.

[Chapter 6](https://automatetheboringstuff.com/chapter6/) - Working with strings and useful string methods

[Chapter 7](https://automatetheboringstuff.com/chapter7/) - Searching strings for patterns using regular expressions