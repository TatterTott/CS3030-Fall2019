import requests
import json

class StartingEquipment():

    def __init__(self):
        self.startingEquipmentURL = 'http://www.dnd5eapi.co/api/startingequipment/'
        self.equipmentLinks = self.getEquipmentLinks()

    #get data from website given a specific url
    def getUrlData(self, class_url):
        response = requests.get(class_url)
        response.raise_for_status()
        raceJson = json.loads(response.text)
        return raceJson

    def getEquipmentLinks(self):
        urlData = self.getUrlData(self.startingEquipmentURL)
        links = urlData["results"]
        equipmentLinks = {}
        for i in range(len(links)):
            key = links[i]['class']
            val = links[i]['url'][-1]
            equipmentLinks[key] = val
        return equipmentLinks

    def chooseStartingEquipment(self, character, menuOption):

        if menuOption == 'quick':
            equipmentURL = self.startingEquipmentURL + self.equipmentLinks[character.char_class]
            equipmentJSON = self.getUrlData(equipmentURL)
            startingEquipment = equipmentJSON["starting_equipment"]

            for i in range(len(startingEquipment)):
                character.startingEquipment.append((startingEquipment[i]["item"]["name"], startingEquipment[i]["quantity"]))

            itemTuple = character.startingEquipment
            itemTuple = [i[0] for i in itemTuple]
            items = ', '.join(i for i in itemTuple)

            if not any(c.isalpha() for c in items):
                print("By default a " + str(character.char_class) + " starts with no default equipment.")

            else:
                print("By default a " + str(character.char_class) + " starts with " + str(items))

            num_choices = equipmentJSON["choices_to_make"]
            print("Please choose " + str(num_choices) + " from the choices below")
            choices = []

            for i in range(1, num_choices + 1):
                choice = equipmentJSON['choice_' + str(i)]
                dict = {}

                #list of choices for a given option
                for j in range(len(choice)):
                    inner = choice[j]["from"]
                    dict2 = {}

                    for k in range(len(inner)):
                        quantity = inner[k]["quantity"]
                        item = inner[k]["item"]["name"]
                        dict2[k + 1] = {item:quantity}

                    num_inner_choices = choice[j]["choose"]
                    dict[j + 1] = {num_inner_choices:dict2}

                choices.append(dict)

            #[{option#:{num_inner_choices{item:quantity}}}]
            for i in range(len(choices)):
                print("Choice " + str(i + 1) + " has " + str(len(choices[i].keys())) +
                      " option(s) to choose from.")

                for option in choices[i].keys():
                    print("Option " + str(option) + ":")

                    for innerChoices in choices[i][option].keys():
                        print("Choose " + str(innerChoices) + " from this option")

                        for items in choices[i][option][innerChoices].keys():

                            for item, quantity in choices[i][option][innerChoices][items].items():
                                print(quantity, item)
                print('\n')

            inpChoice = input("Choose a choice to select your equipment from"
                              "(Enter a number between 1 and " + str(len(choices)) + "): ")

            inputChoices = [str(i) for i in range(1, len(choices) + 1)]

            if inpChoice not in inputChoices or not inpChoice.isdigit():
                while(inpChoice not in inputChoices or not inpChoice.isdigit()):
                    inpChoice = input(inpChoice + " is not a valid choice. Please enter a number between 1 and " +
                          str(len(choices)) + "): ")

            inpChoice = int(inpChoice) - 1

            for option in range(1, len(choices[inpChoice].keys()) + 1):
                numInner = 0
                itemsList = []
                itemDict = {}

                for innerChoices in choices[inpChoice][option].keys():
                    numInner = innerChoices
                    for items in choices[inpChoice][option][innerChoices].keys():
                        for item, quantity in choices[inpChoice][option][innerChoices][items].items():
                            itemsList.append(item)
                            itemDict[item.lower()] = quantity

                print("Choose " + str(numInner) + " from option " + str(option) + ":")
                itemChoices = ', '.join(i for i in itemsList)
                item_choices = [j.lower() for j in itemsList]

                for j in range(1, numInner + 1):
                    inpOption = input(str(j) + ":").lower()

                    if inpOption.lower() not in item_choices:

                        while (inpOption.lower() not in item_choices):
                            print(inpOption + " is not a valid equipment choice. Choose a piece of equipment from the following:")
                            print(itemChoices)
                            inpOption = input().lower()

                    character.startingEquipment.append((inpOption, itemDict[inpOption]))