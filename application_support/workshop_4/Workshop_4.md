## Application Support - Workshop 4

Today we will be looking at reading and writing from files in Python in more detail.

### Recap

Last week we looked at two collection data types in Python - lists and dictionaries. 
Remember, there are two other collection types - tuples and sets - but they're not 
important for now. 

```python
shopping_list = ["Apples", "Bread", "Milk"]

apples = shopping_list[0]

for food in shopping_list:
    print(food)

print(len(shopping_list))
```

Lists are defined with square brackets, and its items can be of any data type - strings, 
integers, booleans, even other lists. To access a single item in a list we can use the 
index of the item, starting from zero and square brackets. To print all items in a list we
can use a `for in` loop. To find the length of a list we can use the `len()` function.

```python
data = {
    "order_id": "108607243",
    "status": "Dispatched",
    "order_item_id": "106385038",
    "sku": "SOFAGREENVELVET01",
}
print(data["order_id"])
```

Dictionaries are defined using curly brackets with key and value pairs. To access a single
item in a dictionary we can use the key of the item and square brackets.

```python
file = open("demo.txt", "r")
print(file.read())
```

We also started to look at reading files in Python. To read a file in Python we use the 
`open()` function with the name of the file as a parameter to save the file into a 
variable. We can then use the `read()`, `read_line()` or `read_lines()` methods on the 
file to read its contents.

```python
import csv

with open("demo.csv", newline='') as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        print(row)
```

In this example we are using the `with as` statement to open the file in a context, 
meaning we don't have to worry about manually closing our connection to the file. When it 
comes to CSV files we can take the file variable and pass it as a parameter to the 
`DictReader` class to which will create a list of dictionaries for each row, where the key
will be column name and value will be the row data as you can see below.

```python
reader = [
    {
        "order_id": "108607243",
        "status": "Dispatched",
        "order_item_id": "106385038",
        "sku": "SOFAGREENVELVET01",
    },
    {
        "order_id": "108607244",
        "status": "New",
        "order_item_id": "106385039",
        "sku": "CHAIRBLUEWOOD02",
    },
]
```

### Task 1 - Recap
Write a script that will read from a CSV file and print all orders that are in "Cancelled" 
state.

Bonus: Take the CSV filename and state as user input from the command line.

### Writing files
This is very similar to reading and could be useful if we're creating a script that does a
series of actions, and we'd like to automatically save the output in a file, rather than 
just printing to the terminal.

```python
file = open("output.txt", "w")
print(file.write("Hello, World!"))
```

We need to first open or create a file to write to using the `open()` function as before, 
but this time in a writeable mode. So we need to pass `"w"` to the open function. Then 
with this file variable, we can use the `write()` method and pass a string or some data as
a parameter. That's it!

```python
import csv

with open("demo.csv", "w") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["order_id", "status"])
    writer.writerow(["108607244", "New"])
```

For CSV files however, it's more useful for us to use the csv module, as we did when 
reading. Here we use the `csv_file` variable and pass it to the `writer()` function from 
the csv module to create a `writer` variable. This `writer` variable then has a 
`writerow()` method which we can pass a list of values as our row content which it will 
write to the CSV file.

### Task 2 - Writing Files
Write a script that will read from one CSV and write all orders to another CSV file that
are in "Cancelled" state.
