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
        for i in range(len(classJson["proficiency_choices"])):
            #check to see if its a skill list
            if classJson["proficiency_choices"][i]["from"][0]["name"][:7] == "Skill: ":
                max_number_of_skills = classJson["proficiency_choices"][i]["choose"]
                print(
                    "A " + str(character.char_class) + " can have " + str(max_number_of_skills) + " proficient skills.")
                print("Enter your proficient skills:")
                prof_Json = classJson["proficiency_choices"][i]["from"]
                prof_choices = []
                for j in range(len(prof_Json)):
                    prof_choices.append(prof_Json[j]["name"][7:])
                choices = ', '.join(i for i in prof_choices)

                prof_choices = [j.lower() for j in prof_choices]
                for j in range(1, max_number_of_skills + 1):
                    inp = input(str(j) + ":").capitalize()
                    if inp.lower() not in prof_choices:
                        while (inp.lower() not in prof_choices):
                            print(inp + " is not a valid skills choice. Choose a skill from the following:")
                            print(choices)
                            inp = input().capitalize()

                    character.prof_skills[inp] = 'Yes'
            #else add to misc tool list
            else:
                max_number_of_tools = classJson["proficiency_choices"][i]["choose"]
                print("A " + str(character.char_class) + " can have " + str(max_number_of_tools) + " proficient tools.")
                print("Enter your proficient tools:")

                toolsJson = classJson["proficiency_choices"][i]["from"]
                tools = []
                for j in range(len(toolsJson)):
                    tools.append(toolsJson[j]["name"])

                choices = ', '.join(j for j in tools)
                tools = [j.lower() for j in tools]

                for j in range(1, max_number_of_tools + 1):
                    inp = input(str(j) + ":")
                    if inp.lower() not in tools:
                        while (inp.lower() not in tools):
                            print(inp + " is not a valid tool choice. Choose a tool from the following:")
                            print(choices)
                            inp = input()

                    character.prof_misc.append(inp)

        weaponProficienciesJson = classJson["proficiencies"]
        for i in range(len(weaponProficienciesJson)):
            character.prof_misc.append(weaponProficienciesJson[i]["name"])

        savingThrowJson = classJson["saving_throws"]
        for i in range(len(savingThrowJson)):
            character.saving_throws[savingThrowJson[i]["name"]] = "Yes"

        character.hit_dice = classJson["hit_die"]




        # print(classJson)
        #TODO: finish this method
