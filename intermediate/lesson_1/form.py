from datetime import datetime, timedelta

from selenium import webdriver

browser = webdriver.Chrome(executable_path="/Users/smistry/Downloads/chromedriver")
browser.get("https://docs.google.com/forms/d/19BfYn9Qyh2cW9yxzJdOJmnKDvGqmAWOzWoYcCdecIvI/edit")

product_types = browser.find_elements_by_class_name("freebirdFormviewerViewItemsRadioOptionContainer")
last_product = product_types[-1]
last_product.click()

product_quantity = browser.find_element_by_class_name("quantumWizTextinputPaperinputInput")
product_quantity.send_keys("110")

order_date = browser.find_element_by_xpath("//input[@type='date']")
order_date.click()

tomorrow = datetime.today() + timedelta(days=1)
order_date.send_keys(tomorrow.strftime("%d%m%Y"))

order_times = browser.find_elements_by_css_selector(
    ".freebirdFormviewerViewItemsTimeTimeInputs .quantumWizTextinputPaperinputInput"
)
order_times[0].send_keys("10")
order_times[1].send_keys("00")

submit_button = browser.find_element_by_class_name("freebirdFormviewerViewNavigationButtons")
submit_button.click()
