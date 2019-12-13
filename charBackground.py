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
                    bg_options = ', '.join(i for i in self.backgounds)
                    print(charBG + ' is not a valid background option.\n'
                          'Please select a background from the following:\n'
                          + bg_options)
                    charBG = input().lower()

            character.backgound = charBG.capitalize()
            self.backgroundStats(character)
    
    def backgroundStats(self, character):
        background = character.backgound
        skills = self.bgDict[background].get("Skills")
        tools = self.bgDict[background].get("Tools")
        langs = self.bgDict[background].get("Languages")
        equip = self.bgDict[background].get("Equipment")



