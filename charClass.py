import requests
import json

class CharClass():

    def __init__(self):
        self.classUrl = 'http://dnd5eapi.co/api/classes/'
        self.classes, self.class_links = self.populateClasses()

    #get data from website given a specific url
    def getUrlData(self, class_url):
        response = requests.get(class_url)
        response.raise_for_status()
        raceJson = json.loads(response.text)
        return raceJson

    # populate the classes array with the classes in the api
    def populateClasses(self):
        classes = []
        class_links = {}
        classJson = self.getUrlData(self.classUrl)

        for charClass in classJson['results']:
            classes.append(charClass['name'])

        i = 1
        for charClass in classes:
            class_links[charClass] = str(i)
            i += 1

        return classes, class_links

    # user chooses a class and this function makes sure it's a valid class
    def chooseClass(self, character, menuOption):

        if menuOption == 'quick':
            print('Please enter a class for your character')
            charClass = input().lower()
            classes = self.classes

            classes = [i.lower() for i in classes]

            if charClass not in classes:
                while charClass not in classes:
                    class_options = ', '.join(i for i in self.classes)
                    print(charClass + ' is not a valid class option.\n'
                                 'Please select a class from the following:\n'
                          + class_options)
                    charClass = input().lower()

            character.char_class = charClass.capitalize()
            self.characterBonuses(character)

    # will fill in the character bonuses
    def characterBonuses(self, character):
        classUrl = self.classUrl + self.class_links[character.char_class]
        classJson = self.getUrlData(classUrl)
        print(classJson)
        #TODO: finish this method