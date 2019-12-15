import requests
import json
from character import Character
from race import Race
from charClass import CharClass
from charBackground import CharBackground
from statRoller import StatRoller
from statCalculator import StatCalculator
from PDFWriter import write_fillable_pdf
from characterDictBuilder import CharacterDictBuilder
from starting_equipment import StartingEquipment

#this class will handle all menu selections
class Menu():
    def __init__(self):
        self.quick = None
        self.detailed = None

    #this method will define whether they want a detailed menu or a quick fill menu going forward
    def menuOption(self):
        exitLoop = False
        #will run as long as they don't input a correct menu option
        while exitLoop == False:
            print("Welcome to the DnD Character Sheet Builder!\n"
                  "Please select either Beginner or Experienced to get started:\n"
                  "1.Experienced\n"
                  "2.Beginner")
            option = input()
            #option 1 is associated with quick menu going forward
            if option == '1':
                self.quick = True
                exitLoop = True
            #option 2 is associated with detailed menu going forward
            elif option == '2':
                self.detailed = True
                exitLoop = True
            #error: not a correct input
            else:
                print(option + ' is not a valid menu option. Please select a valid menu option.\n')

    #master character sheet function
    def buildCharacterSheet(self, character):
        backgroundList = self.getBGs()
    
        #get player name
        print("Please enter the name of the player")
        playerName = input()

        #get character name
        print("Please enter the name of the character")
        characterName = input()

        #setting variables like this for now in case we want to put it in a try/except for
        #error handling later
        character.player_name = playerName
        character.char_name = characterName

        #race class will handle all race attributes
        race = Race()

        charClass = CharClass()

        startingEquipment = StartingEquipment()

        charBackground = CharBackground(backgroundList)


        #race will be filled in depending on menu selection
        if self.quick == True:
            race.chooseRace(character, menuOption='quick')
            charClass.chooseClass(character, menuOption='quick')
            bg = charBackground.chooseBackground(character, menuOption='quick')
            character.background = bg
            startingEquipment.chooseStartingEquipment(character, menuOption='quick')

            StatRoller.rollForStats(character)
            
            StatCalculator.update(character)

            charDict = CharacterDictBuilder.builder(character)
            outFile = characterName+'_char_sheet.pdf'
    
            write_fillable_pdf('.\\CharacterSheetTemplate.pdf',outFile,charDict)
        else:
            race.chooseRace(character, menuOption='detailed')
            charClass.chooseClass(character, menuOption='detailed')
            charBackground.chooseBackground(character, menuOption='detailed')
    
    def getBGs(self):
        response = requests.get("https://api.open5e.com/backgrounds/")
        response.raise_for_status()
        raceJson = json.loads(response.text)


        backDict = {}

        bgs = raceJson['results']
        for bg in bgs:
            backDict[bg.get('name')] = {'Skills':bg.get('skill_proficiencies'),
                                    'Tools':bg.get('tool_proficiencies'),
                                    'Languages':bg.get('languages'),
                                    'Equipment':bg.get('equipment')
                                    }
        return backDict
