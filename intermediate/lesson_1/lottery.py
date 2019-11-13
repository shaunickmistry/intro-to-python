from time import sleep

from selenium import webdriver

browser = webdriver.Chrome(executable_path="/Users/smistry/Downloads/chromedriver")
browser.get("https://www.todaytix.com/x/london/shows/12495-harry-potter-and-the-cursed-child")

sleep(2)
enter_now = browser.find_element_by_css_selector("button[type='submit']")
enter_now.click()

sleep(2)
login_text = browser.find_element_by_class_name("_2k8oOPoivg")
login_text.click()

sleep(2)
email_address = browser.find_element_by_name("email")
email_address.send_keys("shaunickmistry@hotmail.co.uk")

sleep(2)
password = browser.find_element_by_css_selector("input[type='password']")
password.send_keys("test")

sleep(2)
form = browser.find_element_by_css_selector("button[data-testid='signInSignUp_submit_button']")
form.click()

sleep(2)
form = browser.find_element_by_css_selector("form")
form.submit()
