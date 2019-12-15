import requests
import json

class Race():
    def __init__(self):
        self.race_url = 'http://dnd5eapi.co/api/races/'
        self.races, self.race_links  = self.populateRaces()

    #get data from website given a specific url
    def getUrlData(self, race_url):
        response = requests.get(race_url)
        response.raise_for_status()
        raceJson = json.loads(response.text)
        return raceJson

    #populate the races array with the races in the api
    def populateRaces(self):
        races = []
        race_links = {}
        raceJson = self.getUrlData(self.race_url)

        for race in raceJson['results']:
            races.append(race['name'])

        i = 1
        for race in races:
            race_links[race.lower()] = str(i)
            i += 1

        return races, race_links

    #user chooses a race and this function makes sure it's a valid race
    def chooseRace(self, character, menuOption):
        race_options = ', '.join(i for i in self.races)
        races = self.races
        races = [i.lower() for i in races]

        if menuOption == 'detailed':
            print("DnD has a variety of races to choose from. The following are the races that you can choose from.")
            print(race_options)

            while(True):
                moreInfo = input("If you would like to know more about a race, enter the name of the race. If you would\n"
                    "like to continue, enter continue. If you would like to print out the race options again, enter races: ")

                if(moreInfo.lower() != "continue" and moreInfo.lower() not in races and moreInfo.lower() != "races"):

                    while(moreInfo.lower() != "continue" and moreInfo.lower() not in races and moreInfo.lower() != "races"):
                        moreInfo = input(moreInfo + " is not a valid input. Please enter a valid menu option.")

                if(moreInfo.lower() == "continue"):
                    break

                elif(moreInfo.lower() == "races"):
                    print(race_options)

                else:
                    race_url = self.race_url + self.race_links[moreInfo.lower()]
                    raceJson = self.getUrlData(race_url)
                    print(raceJson["alignment"])
                    print(raceJson["age"])
                    print(raceJson["size_description"])

        print('Please enter a race for your character')
        race = input().lower()

        if race not in races:
            while race not in races:
                print(race + ' is not a valid race option.\n'
                             'Please select a race from the following:\n'
                      + race_options)
                race = input().lower()

        if race == 'half-elf':
            character.race = 'Half-Elf'
        elif race == 'half-orc':
            character.race = 'Half-Orc'
        else:
            character.race = race.capitalize()

        self.raceBonuses(character)

    #will fill in the character bonuses(languages, speed, ability bonuses, proficiencies, traits)
    def raceBonuses(self, character):
        race_url = self.race_url + self.race_links[character.race.lower()]
        raceJson = self.getUrlData(race_url)
        character.speed = raceJson['speed']
        character.ability_bonuses = raceJson['ability_bonuses']

        jsonLanguages = raceJson['languages']
        languages = []
        for i in range(len(jsonLanguages)):
            languages.append(jsonLanguages[i]['name'])
        for lang in languages:
            character.languages.append(lang)

        jsonProficiencies = raceJson['starting_proficiencies']
        proficiencies = []
        for i in range(len(jsonProficiencies)):
            prof = (jsonProficiencies[i]['name'])
            if (prof.startswith('Skill')):
                prof = prof[7:]
                character.prof_skills[prof] = 'Yes'
            else:
                character.prof_misc += prof
            

        jsonTraits = raceJson['traits']
        traits = []
        for i in range(len(jsonTraits)):
            traits.append(jsonTraits[i]['name'])
        character.traits = ', '.join(i for i in traits)






