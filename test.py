import requests
import json

def main():
    backgrounds = "https://api.open5e.com/backgrounds/"
    response = requests.get(backgrounds)
    response.raise_for_status()
    raceJson = json.loads(response.text)
    bgs = raceJson['results']
    numOfBackgrounds = len(bgs)
    for bg in bgs:
        print("NAME:",bg.get('name'))
        print("SKILLS:",bg.get('skill_proficiencies'))
        print("TOOLS:",bg.get('tool_proficiences'))
        print("LANGUAGES:",bg.get('languages'))
        print("EQUIPMENT:",bg.get('equipment'))
        print()

main()
