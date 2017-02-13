import urllib
import urllib.request

import lxml as lxml
from bs4 import BeautifulSoup
from bs4 import __all__

url = 'http://www.sportsbet.com.au/betting/soccer?MegaNav'
#url = 'http://www.sportstats.com/soccer/'
#url = 'http://www.google.com.au/'

#Search = 'bet'
#FullUrl = url+'?gfe_rd=cr&ei=ETqgWM7CMNLN8ge3i53IBQ#safe=off&q='+Search

#htmlFile = urllib.request.urlopen(FullUrl)
htmlFile = urllib.request.urlopen(url)
#print(FullUrl)
htmlText = htmlFile.read()

#print(htmlText)

soup = BeautifulSoup(htmlText,"lxml")
#links = soup.find_all("span",{"class" : lambda L: L and L.startswith('price-val')})
links = soup.find_all("div",{"class" : lambda L: L and L.startswith('price-link')})
#print(soup.prettify())

for link in links:
    teams = soup.find_all("span",{"class":"team-name ib"})
    prices = soup("span", {"class": lambda L1: L1 and L1.startswith('price-val')})
   #print(link)
    for team in teams:
        print(team)
        print("chutiya")
        print(prices)
        break
    exit()
