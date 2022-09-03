from bs4 import BeautifulSoup
import requests
import json

class Webscraper():
    def __init__(self):
        # Array to store all the character information we extract
        self.characters = []

    def readPage(self, url):
        req = requests.get(url)
        parse = BeautifulSoup(req.content, "html.parser")

        return parse
    
    def dumpJson(self):
        # Creates and dumps all the characters info into a json file
        with open("character.json", "w") as output:
            json.dump(self.characters, output)

        return "JSON File created."

    def extractData(self, res):
        character = {}

        # Get character name from page
        name = res.find('h1')
        if name != None:
            character['name'] = name.string

        # Get Image
        image = res.find('img')
        if image != None:
            character['image'] = image['src']

        # Gets Age, Birthdate, Gender
        data = res.find_all("div", {"class": "data-point"})
        
        if data != None:
            for d in data:
                txt = d.text.rstrip().split(":")
                character[txt[0]] = txt[1]
            
            print(character)

            if "Gender" in character and character['Gender'] == "Male":
                return

            self.characters.append(character)
            return character
        else:
            return

    def mainLoop(self, max):
        url = "https://anilist.co/character/"

        for i in range(1, max):
            res = self.readPage(url + str(i))

            self.extractData(res)
        
        self.dumpJson()

webscraper = Webscraper()
webscraper.mainLoop(50)