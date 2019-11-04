import bs4
import requests
import sys
import webbrowser


class Lucky:

    def __init__(self):
        search_engine = sys.argv[1:][0]
        if search_engine not in ['google', 'bing']:
            print('Please provide a valid search engine: [\'google\', \'bing\']')
            exit()
        else:
            search_criteria = sys.argv[2:]
            response = requests.get("https://www." + search_engine + ".com/search?q=" + ''.join(search_criteria))
            response.raise_for_status()
            pretty_html = bs4.BeautifulSoup(response.text, features="html.parser")

            search = getattr(self, search_engine)
            results = search(pretty_html)
            links = []
            for result in results:
                link = result.select("a")[0]
                links.append(link.get("href"))

            num_open = min(5, len(links))
            for i in range(num_open):
                webbrowser.open(links[i])

    def google(self, soup):
        print("This search engine is not yet configured. Please use another.")
        exit()

    def bing(self, soup):
        return soup.select(".b_algo")


if __name__ == "__main__":
    lucky = Lucky()
