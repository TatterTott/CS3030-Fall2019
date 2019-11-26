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
            race_links[race] = str(i)
            i += 1

        return races, race_links

    #user chooses a race and this function makes sure it's a valid race
    def chooseRace(self, character, menuOption):

        if menuOption == 'quick':
            print('Please enter a race for your character')
            race = input().lower()
            races = self.races

            races = [i.lower() for i in races]

            if race not in races:
                while race not in races:
                    race_options = ', '.join(i for i in self.races)
                    print(race + ' is not a valid race option.\n'
                                 'Please select a race from the following:\n'
                          + race_options)
                    race = input().lower()

            character.race = race.capitalize()
            self.raceBonuses(character)

    #will fill in the character bonuses(languages, speed, ability bonuses, proficiencies, traits)
    def raceBonuses(self, character):
        race_url = self.race_url + self.race_links[character.race]
        raceJson = self.getUrlData(race_url)
        character.speed = raceJson['speed']
        character.ability_bonuses = raceJson['ability_bonuses']

        jsonLanguages = raceJson['languages']
        languages = []
        for i in range(len(jsonLanguages)):
            languages.append(jsonLanguages[i]['name'])
        character.languages = ', '.join(i for i in languages)

        jsonProficiencies = raceJson['starting_proficiencies']
        proficiencies = []
        for i in range(len(jsonProficiencies)):
            proficiencies.append(jsonProficiencies[i]['name'][7:])
        character.prof_skills = proficiencies

        jsonTraits = raceJson['traits']
        traits = []
        for i in range(len(jsonTraits)):
            traits.append(jsonTraits[i]['name'])
        character.traits = ', '.join(i for i in traits)






