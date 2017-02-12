import urllib
import urllib.request

url = 'https://www.facebook.com/'


htmlFile = urllib.request.urlopen(url)

htmlText = htmlFile.read()

print(htmlText)
