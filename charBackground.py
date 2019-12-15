import requests
import json
import re


class CharBackground():

    def __init__(self,bgDict):
        self.backgrounds = list(bgDict.keys())
        self.bgDict = bgDict

    def chooseBackground(self, character, menuOption):
         if menuOption == 'quick':
            backgrounds = self.backgrounds 
            print("The options available to you are: " + backgrounds[0] + ", " + backgrounds[1] + ", " + backgrounds[2])
            print('Please enter a background for your character')
            charBG = input().lower()

            backgrounds = [i.lower() for i in backgrounds]

            if charBG not in backgrounds:
                while charBG not in backgrounds:
                    bg_options = ', '.join(i for i in self.backgrounds)
                    print(charBG + ' is not a valid background option.\n'
                          'Please select a background from the following:\n'
                          + bg_options)
                    charBG = input().lower()

            if charBG == 'con artist':
                charBG = 'Con Artist'
                character.background = charBG
            else:
                character.background = charBG.capitalize()

            self.backgroundStats(character)

            return charBG.capitalize()

    
    def backgroundStats(self, character):
        background = character.background

        skillStr = self.bgDict[background].get("Skills")
        skills = skillStr.split(", ")
        for elem in skills:
            character.prof_skills[elem] = "Yes"

        tools = self.bgDict[background].get("Tools")
        langs = self.bgDict[background].get("Languages")

        if langs != None and langs.startswith("Two"):
            languageList,languages = self.getLangs()
            print("The options of languages you have to chose from are",languageList)
            print("You know: ")
            backLangs = ""
            for elem in character.languages:
                print(elem)

            languages = [i.lower() for i in languages]

            firstLang = input("please chose a language: ")
            if firstLang.lower() not in languages:
                while(firstLang.lower() not in languages):
                    print(firstLang + " is not a valid language choice. Choose a languages from the following:")
                    print(languageList)
                    firstLang = input().lower

            backLangs += firstLang + ", "

            firstLang = input("please chose another language: ")
            if firstLang.lower() not in languages:
                while(firstLang.lower() not in languages):
                    print(firstLang + " is not a valid language choice. Choose a languages from the following:")
                    print(languageList)
                    firstLang = input.lower()

            backLangs += firstLang
            charLangs = ', '.join(i for i in character.languages) 
            charLangs += ", " + backLangs

        else:
            if langs == None:
                charLangs = ', '.join(i for i in character.languages)
            else:
                charLangs = langs

        if tools == None:   
            pass
        else:
            if tools != None and tools.startswith("Two"):
                character.prof_misc.append("Disquise kit, Forgery Kit")
            else:
                character.prof_misc.append(tools)

        character.prof_misc.append(charLangs)

        equip = self.bgDict[background].get("Equipment")
        character.equipment.append(equip)

    def getLangs(self):
        response = requests.get("http://dnd5eapi.co/api/languages")
        response.raise_for_status()
        langJson = json.loads(response.text)

        languages =[]
        
        for lang in langJson['results']:
            languages.append(lang['name'])

        langString = ""
        for elem in languages:
            langString = ', '.join(i for i in languages)

        return langString,languages
