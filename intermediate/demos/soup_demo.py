import requests

from bs4 import BeautifulSoup

response = requests.get("https://www.google.com")
html = BeautifulSoup(response.text, "html.parser")
account_link = html.select("#button")[0]

print(account_link.attrs)
