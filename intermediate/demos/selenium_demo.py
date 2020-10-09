from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

browser = webdriver.Chrome(executable_path="/Users/smistry/Downloads/chromedriver")
browser.get("https://www.bbc.co.uk/search?q=")
sleep(5)
search_box = browser.find_element_by_id("search-input")
search_box.send_keys("football")
search_box.send_keys(Keys.ENTER)
# browser.close()
