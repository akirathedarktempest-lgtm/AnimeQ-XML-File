#This is now the main file, the first one can't be accessed because now we have two shows, ORV and Oshi No Ko, and it may cause error, but this one will work now perfectly. 
#I have made it by using the previous one and just made a little bit of changes, as the show is not a dictionary now, but a list having more than one show, and each show is a dictionary...it looks confusing, but it is what it is

import xmltodict
import requests
import random

response=requests.get("https://akirathedarktempest-lgtm.github.io/AnimeQ-XML-File/main/AnimeQ.xml")

class Dictionary:
    def __init__(self):
        pass

    dictionary=xmltodict.parse(response.text)

    quotes=dictionary["quotes"]#this opens the main dictionary we get
    description=dictionary["quotes"]["description"]#this is the description of the xml file already given before anything

    def findShow(self):
        show_name=input()
        for j in self.quotes["show"]:
            show=j["name"]
            if show_name!=show:
                pass
            else:
                print(j["name"])
                for i in j["character"]:
                    print(i["character-name"])
                    if type(i["quote"]) is str:#this thing i noticed in experimenting discord bot example and as there is only one quote of Akane, it wasn't a list, it was a str
                        print(i["quote"])
                    elif type(i["quote"]) is list:#and at loop, the indexing was happening at string like character by character, like a\nb\nc and like that, I realized it would cause same here as well so corrected it
                        for z in i['quote']:
                            print(z)
                    else:
                        print("Something is wrong!")#and i will add else because ignoring else can have problem, if the condition is else and if you haven't written it then it will tell you nothing 
                return
        
        print("Can't find the searched show :(")

    def characterQuote(self):
        character_name=input()
        for j in self.quotes["show"]:
            for i in j["character"]:
                if i["character-name"]==character_name:
                    print(i["character-name"])
                    if type(i["quote"]) is str:#yesterday i added Akane to the file having only one quote, and at night I realized...if there's just one quote, then it wouldn't work like list it will start printing character by character
                        print(i["quote"])#it was something serious, so I thought whole night and concluded to use type! I tried it first, it gave character by character, and after adding type, it worked perfectly like I want!
                    elif type(i["quote"]) is list:
                        for z in i["quote"]:
                            print(z)
                    else:
                        print("Something is wrong!")
                    return
                else:
                    pass
        print("Couldn't find the character :(")

    def randomQuote(self):
        show=random.choice(self.quotes["show"])
        character=show["character"]
        character=random.choice(character)
        quote=random.choice(character["quote"])
        print(f"{quote} ~ {character["character-name"]}")

    def characterRandom(self):
        character_name=input()
        show=self.quotes["show"]
        for s in show:
            character=s["character"]
            for i in character:
                if i["character-name"]==character_name:
                    quote=random.choice(i["quote"])
                    print(f"{quote} ~ {i["character-name"]}")
                    return
                else:
                    pass
        print("Can't find any character you searched for :(")

    def showRandom(self):#in this, you will give a name of a show, and it will gave a random quote from a random character in the show
        show=self.quotes["show"]
        name=input()
        for i in show:
            if i["name"]==name:
                character=random.choice(i["character"])
                n=character["character-name"]
                quote=random.choice(character["quote"])
                return print(f"{quote} ~ {n}")
            else:
                pass
        print("Couldn't find a show :(")

dictionary=Dictionary()
dictionary.findShow()
dictionary.characterQuote()
dictionary.randomQuote()
dictionary.characterRandom()
dictionary.showRandom()
