import xmltodict
import requests

response=requests.get("https://akirathedarktempest-lgtm.github.io/AnimeQ-XML-File/main/AnimeQ.xml")


class Dictionary:
    def __init__(self):
        pass
    
    dictionary=xmltodict.parse(response.text)

    quotes=dictionary["quotes"]
    description=dictionary["quotes"]["description"]

    def findShow(self):
        show_name=input()
        show=self.quotes["show"]["name"]
        if show_name!=show:
            print("Sorry, I can't find any such show from my XML :(")
        else:
            print(self.quotes["show"]["name"])
            for i in self.quotes["show"]["character"]:
                print(i["character-name"])
                for z in i['quote']:
                    print(z)

    def characterQuote(self):
        character_name=input()
        character=self.quotes["show"]["character"]
        for i in character:
            if i["character-name"]==character_name:
                print(i["character-name"])
                for z in i["quote"]:
                    print(z)
                return
            else:
                pass
        print("Couldn't find the character :(")

    def randomQuote(self):
        character=self.quotes["show"]["character"]
        character=random.choice(character)
        quote=random.choice(character["quote"])
        print(f"{quote} ~ {character["character-name"]}")

    def characterRandom(self):
        character_name=input()
        character=self.quotes["show"]["character"]
        for i in character:
            if i["character-name"]==character_name:
                quote=random.choice(i["quote"])
                print(f"{quote} ~ {i["character-name"]}")
                return
            else:
                pass
        print("Can't find any character you searched for :(")

dictionary=Dictionary()
dictionary.findShow()
dictionary.characterQuote()
dictionary.randomQuote()#this will give a random quote from a random character
dictionary.characterRandom()#this will give you random quote of a character you searched for, and one more thing, we are still on one sshow only, it will be different when I will add more shows to the XML File

#who thought I don't know OOPS?I have learned it! Anyways, this is how you can access quotes from my XML, but only if there is only one show, as we just have ORV here right now, we just need dictionary
#but if there would be more than one show, then it will be like a list, most probably and at that case, we will do loop most probably? how many times i said most probably...aahhhh! 
#and VS Code was cooking me, I was becoming angry from it...it can't do proper indentation on its own! It was annoying, but now making this gives me relief
#and teach me how to make a folder in this, there will be accessing folder, and the main folder, AnimeQ.xml and updates one
