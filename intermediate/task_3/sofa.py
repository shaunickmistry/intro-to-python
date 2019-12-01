from time import sleep

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# create a selenium webdriver for Chrome
browser = webdriver.Chrome(executable_path="/Users/smistry/Downloads/chromedriver")
# open the Made.com website in a Chrome browser
browser.get("https://www.made.com")

# find the 'account' icon on the page
account_icon = browser.find_element_by_id("my_account_links")
# click it
account_icon.click()

# read user credentials from a file
# change this to a file on your computer
file = open("/Users/smistry/Downloads/user_sofa.txt")
email_address = file.readline()

# find the 'email address' input box
email_address_input = browser.find_element_by_name("login[username]")
# type an email address in
email_address_input.send_keys(email_address)

# find the 'password' input box
password_input = browser.find_element_by_name("login[password]")
password = file.readline()
# type a password in
password_input.send_keys(password)

search_box = browser.find_element_by_id("search-input")
search_box.send_keys("sofa")
# send the 'enter' key to start the search
search_box.send_keys(Keys.ENTER)

# choose the first sofa from the list of results
sofas = browser.find_elements_by_css_selector("#emporio-product-grid div")
sofas[0].click()

# add the sofa to the basket
add_to_basket = browser.find_element_by_css_selector("button[type='submit']")
add_to_basket.click()

# wait for demos purposes and then close the browser
sleep(7)
browser.close()
