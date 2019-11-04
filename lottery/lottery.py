from time import sleep

from selenium import webdriver

browser = webdriver.Chrome(executable_path="/Users/smistry/Downloads/chromedriver")
browser.get("https://docs.google.com/forms/d/19BfYn9Qyh2cW9yxzJdOJmnKDvGqmAWOzWoYcCdecIvI/edit")

email_input = browser.find_element_by_name("email")
email_input.send_keys("bobbuilder@live.com")

firstname_input = browser.find_element_by_name("firstName")
firstname_input.send_keys("Bob")

lastname_input = browser.find_element_by_name("lastName")
lastname_input.send_keys("Builder")

shows = browser.find_elements_by_css_selector(".performances-container > div > label > input")
shows[0].click()

button = browser.find_element_by_class_name("btn-outline")
button.submit()

sleep(10)
browser.close()
