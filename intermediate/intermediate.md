## Intermediate Workshop
This workshop, as mentioned before, is for colleagues that have worked with Python or other programming languages before
and would like to learn about web scraping. It is based on [Chapter 11](https://automatetheboringstuff.com/chapter11/)
from the 'Automate The Boring Stuff' online course.
q

We will be looking at opening web pages with the `webbrowser` module, downloading them with `requests`, formatting with
`Beautiful Soup` and controlling websites using the `Selenium` Python module.

As an example of what you could achieve with this material, see the example program 
[lottery.py](/intermediate/lesson_1/lottery.py) which will enter the lottery for a theatre show Harry Potter and the 
Cursed Child!

### `requests`
This module allows us to download web pages for us to work with later. It doesn't come built in with Python so we'll
need to install it. This can be done by running `pip install requests` from the command line and using `import requests`
in our Python programs. See [Appendix A](https://automatetheboringstuff.com/appendixa/) for more instructions on how to 
install third party modules.

To download a web page with `requests` we use the `requests.get()` method which takes a URL as a parameter, and will 
return a `Response` object containing the web page and some information on the HTTP response in `Response.text`. We can 
check the success of a request by calling the `raise_for_status()` method which will raise an error if there was an
issue.

### `BeautifulSoup`
To continue where the `requests` module left off, `BeautifulSoup` is a module that can extract particular information 
and data from a web response. Again you will need to install it using `pip install beautifulsoup4` and use it in your 
Python programs using `import bs4`.

Web pages are made up of HTML, with certain tags and CSS classes. `BeautifulSoup` allows us to select any DOM object 
from a web page and extra data from it. To do this we call the `bs4.BeautifulSoup()` method with the HTMl to be parsed 
as a parameter. The `BeautifulSoup.select()` method then allows us to use a CSS selector such as `"div.main"` to 
identify a `<div>` tag with the class `main`.

### `webbrowser`
The main usage that we have for the `webbrowser` module is to open web pages using the `open()` method given a URL.  

### Task 1 - Weather Report
With the knowledge given on these web based Python modules, and using 
[Chapter 11](https://automatetheboringstuff.com/chapter11/) of 'Automate The Boring Stuff' write write a Python script 
that will download a weather forecast website web page and print out today's temperature. You'll need to extract the
HTML 

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
Python i.e. `browser = webdriver.Chrome(executable_path="~/Downloads/chromedriver")`.

Using the `get()` method of this webdriver object will then open a web browser that Selenium controls. Next comes 
finding HTML objects on the web page that is open, which can be done using CSS class names, selectors, tag names or ids.
For example, `browser.find_element_by_class_name("main")` would find a single HTML object with the class name `main`
whilst `browser.find_elements_by_class_name("button")` would find all of the HTML objects with class name `button` - 
both returning `WebElement` objects.

Interaction can then occur with these objects through the `click()` and `send_keys()` methods - the latter takes a
string argument and types the string into the given web element.

### Task 3 - Selenium
Now we get onto the fun stuff! Writing programs that can interact with webpages 😱. In this task, use what you have
learnt from Chapter 11 about Selenium to login to a social media account and post a message.

**Top Tips:**
- You'll need to download the `chromedriver` from https://chromedriver.chromium.org/downloads which will allow Python to
talk to your Chrome browser.
- Make sure the `chromedriver` version matches the version of your Chrome application.
- When creating the `browser` variable, pass as a parameter to the Chrome initialiser the location of your file i.e 
`browser = webdriver.Chrome(executable_path="/Users/smistry/Downloads/chromedriver")`
