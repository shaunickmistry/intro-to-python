import bs4
import requests

# get the bbc weather report web page for London
response = requests.get("https://www.bbc.co.uk/weather/2643743")

# check that the HTTP request was successful
response.raise_for_status()

# use the BeautifulSoup module to parse the HTTP response i.e. the web page
pretty_html = bs4.BeautifulSoup(response.text, features="html.parser")

# get a list of all the reported temperatures forecasts for the week
temperatures = pretty_html.select("#daylink-0 .wr-value--temperature--c")

# get the temperature from today's forecast
todays_temperature = temperatures[0].getText()

# print today's temperature forecast the terminal
print(f"Today's temperature is {todays_temperature}C.")
