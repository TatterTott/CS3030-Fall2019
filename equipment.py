import requests
import json

class Equipment():

    def __init__(self):
        self.equipmentURL = 'http://dnd5eapi.co/api/equipment/'
        self.equipmentLinks = self.getEquipmentLinks()

    #get data from website given a specific url
    def getUrlData(self, class_url):
        response = requests.get(class_url)
        response.raise_for_status()
        raceJson = json.loads(response.text)
        return raceJson

    def getEquipmentLinks(self):
        urlData = self.getUrlData(self.equipmentURL)
        links = urlData["results"]
        equipmentLinks = {}
        for i in range(len(links)):
            key = links[i]['name'].lower()
            val = links[i]['url']
            val = [s for s in val.split('/') if s.isdigit()]
            equipmentLinks[key] = val[0]
        return equipmentLinks

    def getEquipmentStats(self, character):

        for i in range(len(character.startingEquipment)):
            equipmentURL = self.equipmentURL + self.equipmentLinks[character.startingEquipment[i][0]]
            equipmentJSON = self.getUrlData(equipmentURL)
            if equipmentJSON["equipment_category"] == "Armor" or equipmentJSON["equipment_category"] == "Adventuring Gear":
                continue
            equipment = equipmentJSON["name"].lower()
            dice_count = equipmentJSON["damage"]["dice_count"]
            dice_value = equipmentJSON["damage"]["dice_value"]
            character.weapon_dict[equipment] = (dice_count, dice_value)