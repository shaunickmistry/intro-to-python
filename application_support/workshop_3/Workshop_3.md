## Application Support - Workshop 3

Today we will be looking at lists, dictionaries and reading from files in Python. 

### Recap

Last week we recapped on `if` and `else` statements and started creating our own functions
in Python. Remember you can define your own function using the `def` keyword, followed by
your function name, parenthesis and some special variable called parameters. 

```python
def my_function(foo, bar):
    print(foo, bar)
    if foo > bar:
        return foo
    return bar
```

Next we looked at one of Python's special variables `__name__` which tells us if this 
Python file is being run as a script or as part of another program. If it is being run as
a script we typically want to run the contents of the script, which is usually placed 
inside of a method called `main()`.

```python
if __name__ == "__main__":
    main()
```

Lastly, we touched on `while` and `for` loops which can help us to run the same code 
multiple times. A `while` loop runs as long as a conditional statement is True, whereas a
`for` loop iterates through a sequence (such as a list of integers).


```python
x = 1
while x < 10:
    print(x)
    x = x + 1
```

You can also see use of the `range()` function which is one of the many in-built functions
in Python, and it will return numbers from 0 to 9.

```python
for x in range(10):
    print(x)
```

### Task 1 - Recap
Write a script that will take a range as input, and print all even numbers in this range.

Bonus: Have a look online at how to pass command line arguments in Python.

### Lists

Lists are a collection data type in Python that allow us to store multiple values in a 
single variable. Think of a real-life example of a list such as a shopping list which is a
list of words, called Strings in Python. So if you were to create such a list object in 
Python, it could look something like this. 

```python
shopping_list = ["Apples", "Bread", "Milk"]
```

We use square brackets to define a list in Python. Items are ordered, changeable, allow 
duplicates and are indexed, starting at 0.

```python
shopping_list = ["Apples", "Bread", "Milk"]
print(shopping_list[0])
```

If we wanted to print the first item of the list, we would give the variable name followed
by square brackets and the index 0. Or if we wanted to print all items in a list we could
use a for loop, defining a variable name for each item in the list as the for loop 
iterates.

```python
shopping_list = ["Apples", "Bread", "Milk"]
for food in shopping_list:
    print(food)
```

### Task 2 - Lists
Use the Python console or a script to create a list and print one, some or all of its 
items. Try using different data types such as Integers and Booleans in your list.

Bonus: Try to add, change and remove items from an existing list.

Lists can hold any data type, so you can have a list of integers, strings, even lists 
within lists, which can be really useful.

```python
shopping_list = [1, 2, "Apple", "Pear", True, False, ["Milk", "Bread", 3, 4]]
```

And we can find out the length of a list by using the `len()` function in Python.

```python
if len(shopping_list) > 10:
    print("You have too much shopping")
```

### Task 3 - List functions
Write a script that will take one shopping item at a time as input, and add it to a list, 
printing each time, but will stop when the word "END" is entered and print the final
contents.

Bonus: Only allow string inputs and a maximum list length of 5.

In total there are 4 collection data types in Python.

- Lists, which we've already seen is a collection type which keeps its order and is 
changeable. It allows duplicate items.
- Tuples are ordered but unchangeable. They also allows duplicate items.
- Sets are unordered and unindexed. It does not allow duplicate items.
- Dictionaries are unordered, changeable and indexed. It also does not allow duplicate items.

This information is "nice to know" for now. It'll hopefully come in handy later on when
we look at the remaining data types. For now though we'll jump to the last collection type
dictionaries, because we want to use these in our scripts.

### Dictionaries

Dictionaries are a way for us to store data in Python using key:value pairs. So instead 
of in a list where we use numeric indexes, we can use a key (normally a string) to extract
a certain value from a dictionary.

```python
data = {
    "order_id": "108607243",
    "status": "Dispatched",
    "order_item_id": "106385038",
    "sku": "SOFAGREENVELVET01",
}
```

To create a dictionary in Python we use the curly brackets and each item requires a 
key:value pair. Values can be any data type, like in lists, including strings, integers,
booleans, lists, and even other dictionaries.

We can change, remove and add items in a dictionary by using a key name.

```python
data["status"] = "Cancelled"
```

Task 4 - Dictionaries
Write a Python script that will create a dictionary and print its content.

Bonus: Try only printing the values of the dictionary, then only the keys, then the key 
and value pairs together, on at a time.

### Reading from files
This is an extremely powerful part of writing scripts with Python, as it can allow you to
have a script that will take a CSV file as input and then perform a series of actions 
using each row.

```python
file = open("demo.txt", "r")
print(file.read())
```

To open a file we use the `open()` built-in function from Python, and pass 2 parameters. 
The first is the filename and the second is the file "mode" that we would like enabled 
i.e. read-only which is "r" or writeable which is "w". There are other modes, but these 
are the most important for now.

We then have a file object, an object is a special data type that can have values and 
defined functions AKA methods (a function is called a method when it is for a specific
object type). One such method for the file object type is `read()` which will return the 
entire contents of a file.

### Task 5 - Read a file
Write a script that will read all lines from a CSV file.

We can now read the entire contents of a file, great! But how about reading a CSV file?

```python
file = open("demo.csv", "r")
print(file.read())
```

Hm, this won't quite cut it. We want to read a CSV file one row at a time.

```python
file = open("demo.csv", "r")
for line in file.readlines():
    print(line)
```

We could use the `readlines()` method in this case, which will return a list of lines in a
file, and can then be used with a for loop to print each line, but there is a better way
to read a CSV file in Python.

```python
import csv

with open("demo.csv", newline='') as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        print(row)
```

Hold on, there's a lot more going on in this example, but I'll explain and all will be 
come clear...er.

Firstly, we have an `import` statement. This is to use some existing Python code from 
another "library" or "module" which is just a collection of useful code that we don't have
to rewrite. In our example we're importing the `csv` module which will allow us to give a
csv file and have a dictionary of all rows in the file.

Then we use the `with` and `as` keywords, this is called a context and requires a bit
more explanation, but imagine it as we're opening the file and the value of the file is 
stored in the `as` variable, in our example `csv_file`.

Lastly, is where we use the `csv.DictReader` class to turn the CSV file into a dictionary.

### Task 6 - Read a CSV file
Write a script to read from a CSV file and print only particular columns from each row.
