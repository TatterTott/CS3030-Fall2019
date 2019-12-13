import requests
import json


class CharBackground():

    def __init__(self,bgDict):
        self.backgrounds = list(bgDict.keys())
        self.bgDict = bgDict

    def chooseBackground(self, character, menuOption):
         if menuOption == 'quick':
            backgrounds = self.backgrounds
            bgString = backgrounds[0]+ ", " + backgrounds[1] + ", " + backgrounds[2]
            print("The options available to you are: "+bgString)
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
            #self.characterBonuses(character)
    
    def characterBonuses(self, character):
        background = character.backgound
        bgInfo = self.backgounds.get(background)
        availSkills = bgInfo.get(skills)

