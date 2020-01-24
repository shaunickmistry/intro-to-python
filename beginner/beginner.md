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
1. Make sure you have the Python programming language installed on your computer.
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
    
    - If you do see this kind of error, then Python is not installed on your computer, and you can use the instructions 
    in [Chapter 0 - Introduction](https://automatetheboringstuff.com/2e/chapter0/) to install it.

2. Pick a piece of software to write Python programs.
    - To start with we will be using the the Python Interpreter to write and run small pieces of Python code, but to 
    write larger programs we will use an Integrated Development Environment (IDE for short). This is mostly just a 
    program to write code, but it has other uses such as highlighting when we've written invalid Python code and running
    code within the software iteself. The IDE that I (and many other developers at Made) use and recommend is 
    [PyCharm Community](https://www.jetbrains.com/pycharm/download), but you are of course free to use any other as they 
    all do the same thing.

### Python interpreter
So let's write our first Python program! And we'll do this using the Python interpreter. This is a piece of software 
that will let you write and run Python instructions one line at a time (not great for writing long programs, but great 
for testing or learning). You can start the interpreter by going to the Terminal/Command Prompt, typing `python` and
then clicking 'Enter' - you should see something like the output below. Your cursor will start after the 3 
chevrons/arrows, and this is where we can write Python commands.

```
$ python
Python 3.8.0 (v3.8.0:fa919fdf25, Oct 14 2019, 10:23:27) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> 
```

In programming, the first line of code we typically write and run prints out the text "Hello, World!" - it's somewhat a 
tradition and checks that everything is setup correctly. So let's start with that shall we?!

```
$ python
Python 3.8.0 (v3.8.0:fa919fdf25, Oct 14 2019, 10:24:53) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> print("Hello, World!")
Hello, World!
```

Great job! If you can see the same output as above you did it! But what did you do? Let's break it down. `print()` is
the first "function" you will have used. A "function" is a block of code that is given a name. Writing the name of 
function with brackets `()` will then mean that you would like to run this block of code.

Then inside of the brackets you wrote some text inside of speech marks `"Hello, World!"`. This is the text (called a 
string in programming, i.e. a string of characters) that we wanted to output to the screen. And that's it! If that 
doesn't make sense, good, keep reading and hopefully it will start to. If it does make sense, even better, but no one 
likes a show off.

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

### Task 1 - Printing and Calculating
Play around with printing messages to the terminal and performing mathematical calculations. 

### Errors are our friends
Errors will happen if code doesn't run, or isn't written, as expected, and that's okay. It just means that we need to 
work out what the problem is and fix it. For example, take a look at the output below, it shows an error that has 
occurred because I've tried to run some invalid code - diving 2 by 0. I thought I'd point this out now, as errors happen
all the time - like life, nothings perfect, so lets not fool ourselves.

```
$ python
Python 3.8.0 (v3.8.0:fa919fdf25, Oct 14 2019, 10:29:27) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> 2 / 0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
```

### Variables
In programming we use variables to store and retrieve data. A variable is like a box with a label on it. The box can 
store certain information, and you can use the label to name the box and remember what's inside of it. In Python we can
store a value in a variable using an assignment statement, this is made up of the variable name, followed by an equals 
sign and the value to be stored. See the example below where we store the number `30` in the variable `age`. Evaluating
the variable `age` then outputs the number `30`.

```
$ python
Python 3.8.0 (v3.8.0:fa919fdf25, Oct 14 2019, 10:29:27) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> age = 30
>>> age
30
```

We can then use these variables later in our program. For example, we can have a program that takes a name as an input
and then then outputs a greeting.

```
$ python
Python 3.8.0 (v3.8.0:fa919fdf25, Oct 14 2019, 10:33:02) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> name = "Shaunick"
>>> print("Hi " + name + " good afternoon!")
Hi Shaunick good afternoon!
```

We can take this one step further by using the `input()` method which prints a message to the user and then takes an 
input  directly from the command line which can be stored in a variable and used in the program.

```
$ python
Python 3.8.0 (v3.8.0:fa919fdf25, Oct 14 2019, 10:35:10) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> name = input("What is your name? ")
What is your name? Shaunick
>>> print("Hi " + name + " good afternoon!")
Hi Shaunick good afternoon!
```

### Task 2 - User Input
Write some Python code that will ask a user for their name and age, and will then output the year that they were born 
i.e. `Hi Shaunick, you were born in 1990`. 