## Application Support Python Workshop

### Introduction
What is Python? Why do we use it? How do we use it? These are some of the questions that we can look to cover in this 
workshop which has been designed to help the Application Support team start their Python programming journey. 

Python is a popular programming language that we use a lot at Made.com and especially in the backoffice team. In its 
simplest form a script/program/application is just a text file (or number of text files) written in a programming
language such as Python, and these files know how to talk to each other. The main purpose of programs and scripts is to
take an input, do something with it and then give an output. 

So we can write a script that takes an order number, or a list of order numbers in the form of a spreadsheet or CSV 
file, creates Eventstore events to marke the orders as cancelled, and then sends them. That's it. Input (an order number
or CSV file), do something (create Eventstore events), output (send them to Eventstore). On a larger scale

And now we just need to learn how to do these things in Python; read a file, create Eventstore events, send them to
Eventstore. Programming, much like life, is all about breaking a problem down into smaller parts, and finding out how to
tackle these small parts. And if you get stuck or see an error message, again, break it down, check that you understand
the input, each line of code, and the output.

```
Note: We can use the same analogy on a larger scale for an application like Hacienda.
    - Input = Eventstore events
    - Do something = check business rules and state of order
    - Output = Send files to warehouses to pick/dispatch/cancel an order
```

### How to read and write Python
So let's jump straight in shall we? Let's take a look at an example of the type of script we can be expected to 
encounter and one day write ourselves. [`raise_hacienda_cancellations.py`](raise_hacienda_cancellations.py) is a script
from Cancellation service and one that the AS team already has some familiarity with. Its job is to take a list of order
items in the form of a CSV file as input and then tell Cancellation service that it can begin the cancellation process
for each order item, which in turn will notify Hacienda but that's less important right now. Lets have a look at how the
script works.

```python
if __name__ == "__main__":
    filepath = "hacienda_cancellation_requests.csv"
    read_csv(filepath)
```

### How to write scripts exercise
