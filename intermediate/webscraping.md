# Web Scraping Workshop
This workshop is for colleagues that have worked with Python or other programming languages before and would like to 
learn about web scraping with Python. It is based on [Chapter 11](https://automatetheboringstuff.com/chapter11/) from 
the 'Automate The Boring Stuff' online course.

We will be looking at opening web pages with the `webbrowser` module, downloading them with `requests`, formatting with
`BeautifulSoup` and controlling websites using the `Selenium` Python module.

As an example of what you could achieve with this material, see the example program 
[lottery.py](/intermediate/demos/lottery.py) which will enter the lottery for a theatre show Harry Potter and the 
Cursed Child!

### `webbrowser`
The main usage that we have for the `webbrowser` module is to open web pages using the `open()` method given a URL.  

```python
import webbrowser

webbrowser.open("https://www.made.com")
```

### `requests`
This module allows us to download web pages for us to work with later. It doesn't come built in with Python so we'll
need to install it. This can be done by running `pip install requests` from the command line and using `import requests`
in our Python programs. See [Appendix A](https://automatetheboringstuff.com/appendixa/) for more instructions on how to 
install third party modules.

To download a web page with `requests` we use the `requests.get()` method which takes a URL as a parameter, and will 
return a Response object containing the web page and some information on the HTTP response in `Response.text`. We can 
check the success of a request by calling the `raise_for_status()` method which will raise an error if there was an
issue.

```python
import requests

response = requests.get("https://www.made.com")
response.raise_for_status()
```

### `BeautifulSoup`
To continue where the `requests` module left off, `BeautifulSoup` is a module that can extract particular information 
and data from a web response. Again you will need to install it using `pip install beautifulsoup4` and use it in your 
Python programs using `import bs4`.

Web pages are made up of HTML, with certain tags and CSS classes. `BeautifulSoup` allows us to select any HTML element 
from a web page and extract data from it. To do this we create a BeautifulSoup object by passing the HTMl to be parsed 
and the parser type as parameters. The `select()` method then allows us to use CSS selectors (see the 
[w3schools.com](https://www.w3schools.com/cssref/css_selectors.asp) tutorial on CSS selectors) such as 
`#my_account_links` to identify an element with an id attribute `my_account_links`. 

```python
import requests

from bs4 import BeautifulSoup

response = requests.get("https://www.made.com")
html = BeautifulSoup(response.text, "html.parser")
account_link = html.select("#my_account_links")
```

### Task 1 - Weather Report
With the knowledge given on these web based Python modules, and using 
[Chapter 11](https://automatetheboringstuff.com/chapter11/) of 'Automate The Boring Stuff' write a Python script that 
will download a weather forecast web page and print out today's temperature. You'll need to identify and extract the
HTML elements containing the forecast data that you're looking for, and then print that to the terminal.

**Top Tips:** 
- Breakdown the problem you have into small, manageable chunks that you understand. 
- Then do the same with the solution that you are trying to create. 
- Try not to get carried away with getting straight to the end result. 
- i.e. How do I download a webpage? Then once that's done, how do I convert that file into a Beautiful Soup object?

### Task 2 - I'm Feeling Lucky
Given a search term, write a Python script that will open the top 5 results from a search engine in your web browser - I
recommend Bing or another search engine as the HTML structure of Google results is complicated for the Selenium module.

### `Selenium`
To control web pages with Python code we can use the Selenium module; where we can click, type and scroll as a user 
would. This can allow us to test websites or automate certain repetitive tasks that we may have. To start using Selenium
we `pip install selenium` and use `from selenium import webdriver` in our programs.

You will need a webdriver file that matches the version of browser you would like Selenium to interact with. For 
example, for Chrome 78 you will need to download the `chromedriver` file from https://chromedriver.chromium.org/ and
either add this executable to your path or add the file location as a parameter when creating your webdriver object in 
Python i.e. `browser = webdriver.Chrome(executable_path="/Users/joebloggs/Downloads/chromedriver")`.

Using the `get()` method of this webdriver object will then open a web browser that Selenium controls. 

Next comes finding HTML objects on the web page that is open, which can be done using CSS class names, selectors, tag 
names or ids. For example, `browser.find_element_by_class_name("main")` would find a single HTML object with the class
name `main` whilst `browser.find_elements_by_class_name("button")` would find all of the HTML objects with class name 
`button` - both returning `WebElement` objects. See 
[Table 11-3](https://automatetheboringstuff.com/chapter11/#calibre_link-11) in Chapter 11 for a list of Selenium methods
to find elements.

Interaction can then occur with these objects through the `click()` and `send_keys()` methods - the latter takes a
string argument and types the string into the given web element.

```python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome(executable_path="/Users/joebloggs/Downloads/chromedriver")
browser.get("https://www.made.com")

search_box = browser.find_element_by_id("search-input")
search_box.send_keys("table")
search_box.send_keys(Keys.ENTER)
```

### Task 3 - Selenium
Now we get onto the fun stuff! Writing programs that can interact with web pages 😱. In this task, use the information 
about Selenium above and [Chapter 11](https://automatetheboringstuff.com/chapter11/) to login to Made.com with your 
customer account and place a sofa in your checkout basket.