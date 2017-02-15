import urllib.request
from bs4 import BeautifulSoup

sports = ["cricket","soccer","boxing","snooker","basketball"]

#urls = ["http://www.sportsbet.com.au/betting/soccer?MegaNav", "http://www.sportsbet.com.au/betting/cricket?MegaNav",
 #       "http://www.sportsbet.com.au/betting/snooker?MegaNav", "http://www.sportsbet.com.au/betting/basketball?MegaNav"]

for sport in sports:

    url = "http://www.sportsbet.com.au/betting/"+sport+"?MegaNav"
    print(url)
    htmlFile = urllib.request.urlopen(url)
    htmlText = htmlFile.read()
    soup = BeautifulSoup(htmlText, "lxml")
    links = soup.find_all("div", {"class": lambda l: l and l.startswith('price-link')})

    for link in links:
        team = link("span", {"class": "team-name ib"})[0].string
        rate = link("span", {"class": lambda l1: l1 and l1.startswith('price-val')})[0].string
        print(team+rate)
    print("Next Sports")
