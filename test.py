import requests
import json

def main():
    bgDict = getBG()
    charaBack = "Acolyte"

    print(bgDict[charaBack].get("Skills"))
    print(bgDict[charaBack].get("Tools"))
    print(bgDict[charaBack].get("Languages"))
    print(bgDict[charaBack].get("Equipment"))

    equip = bgDict[charaBack].get("Equipment")

def getBG():
    response = requests.get("https://api.open5e.com/backgrounds/")
    response.raise_for_status()
    raceJson = json.loads(response.text)

    backDict = {}

    bgs = raceJson['results']
    for bg in bgs:
            backDict[bg.get('name')] = {'Skills': bg.get('skill_proficiencies'),
                                        'Tools': bg.get('tool_proficiencies'),
                                        'Languages': bg.get('languages'),
                                        'Equipment': bg.get('equipment')
                                        }

    return backDict

main()
