import urllib.request
from bs4 import BeautifulSoup

urls = ["https://www.sportsbet.com.au/account?HeaderAccountNo"]

for url in urls:

    htmlFile = urllib.request.urlopen(url)
    htmlText = htmlFile.read()
    soup = BeautifulSoup(htmlText, "lxml")
    links = soup.find_all("div", {"class": lambda l: l and l.startswith('price-link')})
    print(htmlText)
    """for link in links:
        team = link("span", {"class": "team-name ib"})[0].string
        rate = link("span", {"class": lambda l1: l1 and l1.startswith('price-val')})[0].string
        print(team+rate)
    print("Next Sports")
"""