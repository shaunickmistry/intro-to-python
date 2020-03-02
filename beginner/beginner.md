## Beginner Workshop
Python is a popular programming language and one that we use at Made.com for our back-office computer software. In this 
workshop we will be looking at the basics of Python and programming including; variables, functions and conditionals. It
is based on [Chapter 1 - Python Basics](https://automatetheboringstuff.com/2e/chapter1) and 
[Chapter 2 - Flow Control](https://automatetheboringstuff.com/2e/chapter2) from the 'Automate The Boring Stuff' online 
course by Al Sweigart.

As an example of what you could achieve with Python after some study and understanding, see the example programs in 
the [/intermediate](/intermediate) workshop. These include the program [weather.py](/intermediate/task_1/weather.py) 
which will print today's temperature from BBC Weather, [lucky.py](/intermediate/task_2/lucky.py) which given a search 
term, will open the first 5 results in Google for you and [sofa.py](/intermediate/task_3/sofa.py) which will login to 
your Made.com account and buy a sofa. My favourite of example of how we can use programming to automate everyday life is
a program that I've written called [lottery.py](/intermediate/demos/lottery.py) which will automatically login and enter
you in for the lottery for the Harry Potter and the Cursed Child theatre show!

### Before we can start
1. Make sure you have Python 3 installed on your computer.
    - You can check this by opening the Terminal program on Mac or Command Prompt program on Windows and typing 
    `python --version` then hitting enter. 
    
    ```
    $ python --version
    Python 3.8.0
    ```
    
    The version number can be different, but as long as it's not Python 2 or you don't see an error like the one below, 
    you're good to go.
    
    ```
    $ python --version
    -bash: python: command not found
    ```
    
    - If you do see this kind of error, or you have Python 2 installed, you can download Python 3 from 
    [https://www.python.org/downloads/](https://www.python.org/downloads/).

2. Pick a piece of software to write Python programs.
    - To start with we will be using the the Python Interpreter to write and run small pieces of Python code, this comes
    with the Python language on installation. To write larger programs we will use an Integrated Development Environment 
    (IDE for short). This is mostly just a text editor, but it has other uses such as highlighting when we've written 
    invalid Python code and running code easily. The IDE that I (and many other developers at Made) use and recommend is 
    [PyCharm Community](https://www.jetbrains.com/pycharm/download), but you are of course free to use any other as they 
    all do the same thing.

### Python interpreter
So let's write our first Python program! And we'll do this using the Python Interpreter. This is a piece of software 
that will let you write and run Python instructions one line at a time (not great for writing long programs, but super 
for testing or learning). You can start the Interpreter by going to the Terminal/Command Prompt, typing `python` and
hitting 'Enter' - you should see something like the output below. Your cursor will start after the 3 
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
Python 3.8.0 (v3.8.0:fa919fdf25, Oct 14 2019, 10:23:27) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> print("Hello, World!")
Hello, World!
```

Great job! If you can see the same output as above, you did it! But what did you do? Let's break it down. `print()` is
the first "function" you will have used. A "function" is a block of code that is given a name. Writing the name of 
function with brackets `()` will then mean that you would like to run this block of code, also known as executing.

Then inside of the brackets you wrote some text inside of speech marks `"Hello, World!"`. This is the text (called a 
string in programming, i.e. a string of characters) that we wanted to output to the screen. When we give a function some
input data, this is called a parameter. And that's it! If that doesn't make sense, good, keep reading and hopefully it 
will start to. If it does make sense, even better, but no one likes a show off.

Tip: To close the interpreter, type `exit()` and then hit 'Enter'.

Next lets try playing with some numbers. In Maths we "evaluate" an expression by performing a series of actions with 
numbers. We can use Python to do this for us by using the format below - try it out, and play around with other things. 
You can use [Table 1-1](https://automatetheboringstuff.com/2e/chapter1#calibre_link-1652) for more explanation.

```
$ python
Python 3.8.0 (v3.8.0:fa919fdf25, Oct 14 2019, 10:23:27) 
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

#### Bonus
How would you calculate 2 to the power of 4? Tip: As programmers we don't need to know or remember everything, we can 
use online resources to find out and learn!

### Errors are our friends
Errors will happen if code doesn't run, or isn't written, as expected, and that's okay. It just means that we need to 
work out what the problem is and fix it. For example, take a look at the output below, it shows an error that has 
occurred because I've tried to run some invalid code - diving 2 by 0. I thought I'd point this out now, as errors happen
all the time - like life, nothings perfect, so lets not fool ourselves.

```
$ python
Python 3.8.0 (v3.8.0:fa919fdf25, Oct 14 2019, 10:23:27) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> 2 / 0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
```

### Variables
In programming we use variables to store and retrieve data. A variable is like a box with a label on it. The box can 
store certain information, and the label helps us to remember what's inside of the box. In Python we can store a value 
in a variable using an assignment statement, this is made up of the variable name, followed by an equals sign and the 
value to be stored. See the example below where we store the number `30` in the variable `age`. Evaluating the variable 
`age` then outputs the number `30`.

```
$ python
Python 3.8.0 (v3.8.0:fa919fdf25, Oct 14 2019, 10:23:27) 
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
Python 3.8.0 (v3.8.0:fa919fdf25, Oct 14 2019, 10:23:27) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> name = "Shaunick"
>>> print("Hi " + name + ", good afternoon!")
Hi Shaunick, good afternoon!
```

We can take this one step further by using the `input()` function which prints a message to the user and stores user 
input in a variable.

```
$ python
Python 3.8.0 (v3.8.0:fa919fdf25, Oct 14 2019, 10:23:27) 
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

### Creating and running Python programs
You know how to run some individual lines of Python code, great! Next is piecing these lines of code together in a 
Python file to create a program that can be executed i.e. not having to write and execute each line individually in the 
Python interpreter. This can be as simple as taking the `"Hello, World!"` code that we had earlier, and saving it in a 
file with a `.py` extension i.e. a Python file. See my example of the `hello.py` file below.

```python
print("Hello, World!")
```

To run this we can use our terminal, and pass the name of the Python file to the `python` command.

```
$ python hello.py
Hello, World!
```

### Task 3 - Create a program
Try creating a program that takes an input from the user and prints a message to the user, in a Python file.

### Controlling code flow
When we write a program, we don't always want every line of code to be executed. For example, if we ask a user to give
their age as an input, we may want to check that the input is an integer, and not a date or string of characters, as 
this could break our program. This is where boolean values and conditional statements can help us to direct the "flow" 
of code in our program.

The Boolean data type only has two possible values `True` and `False`. It can be used to record if something was 
successful or not and to check for a particular condition i.e. is x greater than or equal to 10. See 
[Table 2-1](https://automatetheboringstuff.com/2e/chapter2#calibre_link-1534) for a list of possible comparison 
operators, these are symbols that can compare two values and evaluate them to a Boolean value.

```
$ python
Python 3.8.0 (v3.8.0:fa919fdf25, Oct 14 2019, 10:23:27) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> x = 10
>>> x >= 10
True
```

Here we can see that x is greater than or equal to 10, so Python returns us the Boolean value `True`. 

A useful control statement is the `if` statement and allows us to decide whether or not we should execute a particular
block of code. We do this by using the `if` keyword in Python followed by a condition - that is an expression that
evaluates to `True` or `False`. Below is a program `ten.py` which shows how this could look. 

```python
x = 10
if x >= 10:
    print("x is greater than or equal to 10")
```

Running `ten.py` would then give the following output.

```
$ python ten.py
x is greater than or equal to 10
```

### Task 4 - If statements
Write a program that will ask the user to guess a secret number, and print if they are correct or not.

#### Bonus
Adapt this program so that it says whether the user's guess is higher or lower, until the user can guess the exact 
number.

Tip: Use the `while` conditional statement.