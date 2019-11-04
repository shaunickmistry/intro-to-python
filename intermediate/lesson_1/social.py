from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--disable-infobars")
options.add_argument("--disable-extensions")
options.add_experimental_option("prefs", {
    "profile.default_content_setting_values.notifications": 1
})
browser = webdriver.Chrome(options=options, executable_path="/Users/smistry/Downloads/chromedriver")

browser.get("https://www.facebook.com")

email_input = browser.find_element_by_id("email")
email_input.send_keys("Your email address")
password_input = browser.find_element_by_id("pass")
password_input.send_keys("Your password")
password_input.submit()

post_box = browser.find_element_by_xpath("//*[@name='xhpc_message']")
post_box.send_keys("This is a test post using Selenium.")

buttons = browser.find_elements_by_tag_name("button")
for button in buttons:
    if button.text == "Post":
        button.click()

sleep(5)
browser.close()
