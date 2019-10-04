import bs4
import requests

response = requests.get("https://www.bbc.co.uk/weather/2643743")
response.raise_for_status()
pretty_html = bs4.BeautifulSoup(response.text, features="html.parser")

elements = pretty_html.select("#daylink-0 .wr-value--temperature--c")
todays_temp = elements[0].getText()

print(f"Today's temperature is {todays_temp}C.")
