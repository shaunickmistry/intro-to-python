import bs4
import requests
import sys
import webbrowser

# get the last argument from the command line i.e. the search criteria
search_criteria = sys.argv[-1]

# search bing.com for the search criteria
response = requests.get("https://www.bing.com/search?q=" + search_criteria)

# check that the HTTP request was successful
response.raise_for_status()

# use the BeautifulSoup module to parse the HTTP response i.e. the web page
pretty_html = bs4.BeautifulSoup(response.text, features="html.parser")

# filter the search results from the web page
results = pretty_html.select(".b_algo")
links = []

if len(results) == 0:
    print("No results found for search criteria: " + search_criteria)
    exit()

# extract a list of web links from the search results
for result in results:
    link = result.select("a")[0]
    links.append(link.get("href"))

# open at most the first 5 web pages
num_open = min(5, len(links))
for i in range(num_open):
    webbrowser.open(links[i])

