# Intro to Python
A series of workshops for MADE employees to automate everyday computer tasks using the online, free course Automate The 
Boring Stuff (https://automatetheboringstuff.com/) by Al Sweigart.

To get the most out of our time in the workshops, chapters and lessons from the course will be assigned _before_ every 
workshop as homework, and the time in the workshop will be used to cover questions and provide 1-to-1 support.

The course includes a series of YouTube videos (links in the below pages) that contain the same content as the text, so
feel free to use whichever works best for you.

## Lesson 0 - Warm Up
The first 6 chapters of Automate The Boring Stuff cover all the basics of Python that you need for this course, so
please read chapters 0-5 and we will cover any questions that you have in Workshop 0. Work along with the examples and 
test your learning with the questions in each chapter. If you have any questions that you'd like to ask before our 
workshop, post them on the Made Slack channel `#python-workshops` and someone will get back to you in a jiff.

[Chapter 0](https://automatetheboringstuff.com/chapter0/) - An introduction to setting up your computer with Python and the software required

[Chapter 1](https://automatetheboringstuff.com/chapter1/) - The basics of the Python programming language (expressions, integers, strings and variables)

[Chapter 2](https://automatetheboringstuff.com/chapter2/) - Controlling the flow of programs (booleans, comparison operators, conditions, if statements, while loops, 
for loops, importing modules)

[Chapter 3](https://automatetheboringstuff.com/chapter3/) - What are functions, global and local scope and exception handling 

[Chapter 4](https://automatetheboringstuff.com/chapter4/) - The list and tuple data types and methods

[Chapter 5](https://automatetheboringstuff.com/chapter5/) - The dictionary data type and structuring data with them

[Chapter 6](https://automatetheboringstuff.com/chapter6/) - Working with strings and useful string methods

The next 4 chapters are extremely useful to get the most out of these workshops, but that's a lot of reading, so they're
not mandatory.

[Chapter 7](https://automatetheboringstuff.com/chapter7/) - Searching strings for patterns using regular expressions

[Chapter 8](https://automatetheboringstuff.com/chapter8/) - Reading and writing files

[Chapter 9](https://automatetheboringstuff.com/chapter9/) - Copying, moving, renaming and compressing files

[Chapter 10](https://automatetheboringstuff.com/chapter10/) - Debugging your code and fixing issues 🐛

## Lesson 1 - Web Scraping
What the bloody hell is web scraping??? Do we take a shovel and start running it across our computer screens? Well 
obviously not, but it actually isn't that far from the analogy of shovelling data from a website into your own program.
Web scraping is the term used to describe a program that downloads data from a website, processes it and produces an 
output. That output could be a report of all the products that a competitor is selling for cheaper, or any updates to a
website since the program last ran.

Have a read of [Chapter 11](https://automatetheboringstuff.com/chapter11/) from Automate The Boring Stuff and Al will 
explain the `webbrowser` builtin module, opening web pages and downloading them, formatting web pages with `Beautiful 
Soup` and controlling websites using the `Selenium` Python module.

### Task 1 - Weather Report
Given a weather reporting website of your choice, write a Python script that will print out today's temperature.

**Top Tips:** 
- Breakdown the problem you have into small, manageable chunks that you understand. 
- Then do the same with the solution that you are trying to create. 
- Try not to get carried away with getting straight to the end result. 
- i.e. How do I download a webpage? Then once that's done, how do I convert that file into a Beautiful Soup object?

### Task 2 - I'm Feeling Lucky
Given a search term, write a Python script that will open the top 5 results from Bing in your web browser.
(I recommend Bing because the HTML structure of Google results has become more complicated since Al wrote his course)

## Lesson 2 - Spreadsheet Manipulation
Bar