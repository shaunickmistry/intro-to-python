from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome(executable_path="/Users/smistry/Downloads/chromedriver")
browser.get("https://www.made.com")

search_box = browser.find_element_by_id("search-input")
search_box.send_keys("table")
search_box.send_keys(Keys.ENTER)

browser.close()
