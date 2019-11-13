## Intermediate Workshop
The intermediate workshop, as mentioned before, is for colleagues that have worked with Python or other programming 
languages before and would like to learn about web scraping.

We will be looking at the `webbrowser` builtin module, opening web pages and downloading them, formatting web pages with
`Beautiful Soup` and controlling websites using the `Selenium` Python module.

As an example of what you could achieve with this material, see the example program 
[lottery.py](/intermediate/lesson_1/lottery.py) which will enter the lottery for a theatre show Harry Potter and the 
Cursed Child!

#### Task 1 - Weather Report
Given a weather reporting website of your choice, write a Python script that will print out today's temperature.

**Top Tips:** 
- Breakdown the problem you have into small, manageable chunks that you understand. 
- Then do the same with the solution that you are trying to create. 
- Try not to get carried away with getting straight to the end result. 
- i.e. How do I download a webpage? Then once that's done, how do I convert that file into a Beautiful Soup object?

#### Task 2 - I'm Feeling Lucky
Given a search term, write a Python script that will open the top 5 results from Bing in your web browser - I recommend
Bing because the HTML structure of Google results has become more complicated since Al wrote his course.

#### Task 3 - Selenium
Now we get onto the fun stuff! Writing programs that can interact with webpages 😱. In this task, use what you have
learnt from Chapter 11 about Selenium to login to a social media account and post a message.

**Top Tips:**
- You'll need to download the `chromedriver` from https://chromedriver.chromium.org/downloads which will allow Python to
talk to your Chrome browser.
- Make sure the `chromedriver` version matches the version of your Chrome application.
- When creating the `browser` variable, pass as a parameter to the Chrome initialiser the location of your file i.e 
`browser = webdriver.Chrome(executable_path="/Users/smistry/Downloads/chromedriver")`

### Lesson 5 - Spreadsheet Manipulation
TBC