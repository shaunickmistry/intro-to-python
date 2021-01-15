## Application Support - Workshop 5

Today we will be looking at reading and writing from databases in Python.

### Recap

In our last workshop we looked at reading and writing from files. To read a file in Python
we use the `open()` function with the name of the file as a parameter to save the file 
into a variable.

In the example below we also pass an additional parameter to the `open()` function. This 
is the `newline` parameter which says to replace `\n` newline characters with `""` an 
empty string. Here we use a "keyword argument" which means that we define the name of the
parameter/argument when calling the function. This is because the function has many
parameters that it can accept, which have default values if you don't specify them, but if
you want to specify them and skip others, you need to pass this as a keyword argument.  

```python
import csv

with open("demo.csv", newline='') as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        print(row)
```

When writing to CSV files we use the `writer()` and `writerow()` functions from the csv 
module.

```python
import csv

with open("demo.csv", "w") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["order_id", "status"])
    writer.writerow(["108607244", "New"])
```

### Task 1 - Recap
Write a script that will read a shopping list from a CSV file with `item,quantity` as the
CSV headers and print its contents to the terminal.

### Reading from databases
To read from databases in Python we first need to open a connection to that database, much
like how we open a file using the `with as` keywords to create a "context". Below you can
see that we create a `connection` variable using a `connect` function, we'll go into that 
afterwards. All you need to know right now is that this creates a connection and session 
with the database.

We then pass the `connection` variable to the `closing()` function from the `contextlib`
module. This will ensure that our connection is closed once we are finished with it. The
`connection` variable has a `cursor()` function which returns a cursor. A cursor allows us
to execute SQL commands on the database within the database session.

Next we execute a `run_sql_query()` function, which we will again come to, but for now 
consider that it will run a SELECT SQL query and return resulting rows. We can then print
these results to the terminal.

```python
import contextlib
import getpass

def main():
    connection = connect(db_host, password)

    with contextlib.closing(connection.cursor()) as cursor:
        results = run_sql_query(cursor)
        print("Results where: ", results)
```

Jumping back to the `connect()` function, it uses the `connect()` function from the 
`mysql.connector` module to create a connection to a PostGres database. To do this we must
pass a series of parameters including database hostname and password. 

```python
import psycopg2

def connect(db_host, password):
    return psycopg2.connect(
        dbname='hacienda',
        host=db_host,
        port=5432,
        password=password,
        user='hacienda'
    )
```

And an example of our `run_sql_query()` function will use a multiline string variable 
(created) using the triple `"""` quotation symbols to create our SQL query. This is then
passed to the `execute()` method of the `cursor` object, which we can then retrieve the 
results from by using the `fetchall()` metod of the `cursor` object.

Note: You will need to install the python modules `contextlib` and `psycopg2` via pip.

```python
def run_sql_query(cursor):
    sql = """
        SELECT *
        FROM order_consignments
        WHERE order_consignments.warehouse_code = 'londongateway';
    """

    cursor.execute(sql)
    return cursor.fetchall()
```

This will return a variable of type list, where each element in the list is a tuple 
(similar to a list). For example of our `order_consignments` database table had the 
columns `id,reference,warehouse_code` and there were 3 such rows in the database where
`warehouse_code` was equal to `londongateway` then we would receive a variable like this:

```python
results = [
    (65, 108905298, 'londongateway'),
    (59, 107645783, 'londongateway'),
    (12, 106476904, 'londongateway'),
]
```

Note: To connect to Made databases you will need to be on the VPN.

### Task 1 - Read from a database
Write a script that will connect to a test database and query a particular table.

### Writing to databases
The only difference with writing to a database in Python is the SQL query. We can use the 
same connection, cursor and content manager that we have when reading. Here you can see 
that we are creating our SQL query, but we're also adding a parameter by passing a tuple 
as the 2nd argument in the `cursor.execute()` method with our `consignment_id` variable.

```python
def write_to_database(cursor, consignment_id):
    sql = """
    UPDATE order_instructions SET state = 'Cancelled' WHERE consignment_id IN %s
    """
    cursor.execute(sql, (consignment_id, ))
```

### Task 2 - Write to a database
Write a script that will read a CSV file of order IDs and their states, and if they are in
'Cancelled' state in a test database update them again to 'Cancelled'.
