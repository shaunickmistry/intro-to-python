# Intro to Python
A course for programming beginners to get hands on with Python (based on https://automatetheboringstuff.com/) by 
automating everyday computer tasks.

# Setup
You will need to check that your computer has the Python programming language installed and a special Python text editor
called IDLE. You can use any text editor, but IDLE includes an interactive shell where you can write Python 
code and see instant results.

1. Search for the IDLE software application on your computer (if you have this, you will also have the Python 
programming language).
2. If you do not have IDLE installed you can download it from here https://www.python.org/downloads/

# Lesson 0
In programming, we start counting at 0 because 0 is where you are now. 1 is where you will go next, and so on.
Programming is all about efficiency you see. As we start looking at programming constructs such as arrays this will 
become more clear. If you're not convinced check out this article 
https://skillcrush.com/2013/01/17/why-programmers-start-counting-at-zero/.

So lesson 0 is some background on Python and programming. Let's learn by doing things, start by opening up IDLE! It
should look something like this.

```
Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 16:52:21) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>>
```

We can write our first ever program by writing the following after the chevrons `>>>`.

```
Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 16:52:21) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> print("Hello, World!")
```

This line of code, when executed/run will print the text `Hello, World!` to the console.

```
Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 16:52:21) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> print("Hello, World!")
Hello, World!
```

Let's break down what this line of code is doing. `print()` is an inbuilt Python function. That means it's some code
that comes with Python for free. Neat! 

But wait, what's a function? I'm glad you asked avid reader. A function is just a grouping of code, and when this code 
is grouped into a function, it can be run by simply writing the name of the function an parentheses/curly brackets.

Next, we can give our functions extra information by passing parameters. A parameter is a piece of information that we
pass in the parentheses of a function. In our example above we passed the text/string `"Hello, World!"` to the `print()` 
function, and so that's what it printed to the console.
