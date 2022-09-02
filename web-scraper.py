from bs4 import BeautifulSoup
import requests

class Webscraper():
    def __init__(self):
        self.data = {}

    def readPage(self, url):        
        req = requests.get(url)
        parse = BeautifulSoup(req.content, "html.parser")

        return parse

    def extractData(self, url):
        res = self.readPage(url)

        character = {}

        name = res.find('h1')
        character['name'] = name.text

        image = res.find('img')
        character['image'] = image['src']

        # Gets Age, Birthdate, Gender
        data = res.find_all("div", {"class": "data-point"})
        for d in data:
            txt = d.text.rstrip().split(":")
            character[txt[0]] = txt[1]


        print(character)




webscraper = Webscraper()
webscraper.extractData("https://anilist.co/character/2")