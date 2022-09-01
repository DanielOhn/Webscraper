from bs4 import BeautifulSoup
import requests

class Webscraper():
    def __init__(self):
        pass

    def readPage(self, url):        
        req = requests.get(url)
        parse = BeautifulSoup(req.content, "html.parser");

        return parse


webscraper = Webscraper()
print(webscraper.readPage("https://anilist.co/character/2"))