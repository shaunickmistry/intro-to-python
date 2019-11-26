from time import sleep

from selenium import webdriver

# create a selenium webdriver for Chrome
browser = webdriver.Chrome(executable_path="/Users/smistry/Downloads/chromedriver")
# open the Harry Potter theatre show ticket website in a Chrome browser
browser.get("https://www.todaytix.com/x/london/shows/12495-harry-potter-and-the-cursed-child")

# wait for the page to load
sleep(2)
# find the 'enter now' button on the page
enter_now = browser.find_element_by_css_selector("button[type='submit']")
# click it
enter_now.click()

sleep(2)
# find the 'login' text on the page
login_text = browser.find_element_by_class_name("_2k8oOPoivg")
# click it
login_text.click()

# read user credentials from a file
# change this to a file on your computer
file = open("/Users/smistry/Downloads/user_lottery.txt")
email_address = file.readline()

sleep(2)
# find the 'email address' input on the page
email_address_input = browser.find_element_by_name("email")
# enter an email address
email_address_input.send_keys(email_address)

sleep(2)
# find the 'password' input on the page
password_input = browser.find_element_by_css_selector("input[type='password']")
# read password from file
password = file.readline()
# enter a password
password_input.send_keys(password)

sleep(2)
# find the form on the next page
form = browser.find_element_by_css_selector("form")
# submit/click it to enter the ticket lottery
form.submit()

# wait for demo purposes and then close the browser
sleep(4)
browser.close()
