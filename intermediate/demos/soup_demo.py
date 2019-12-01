import requests

from bs4 import BeautifulSoup

response = requests.get("https://www.made.com")
html = BeautifulSoup(response.text, "html.parser")
account_link = html.select("#my_account_links")[0]

print(account_link.attrs)
