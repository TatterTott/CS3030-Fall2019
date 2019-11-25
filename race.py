import requests
import json

class Race():
    def __init__(self):
        self.race_url = 'http://dnd5eapi.co/api/races/'
        self.races = self.populateRaces()

    def populateRaces(self):
        races = []
        response = requests.get(self.race_url)
        response.raise_for_status()
        raceJson = json.loads(response.text)

        for race in raceJson['results']:
            races.append(race['name'])

        return races

    def chooseRace(self, character, menuOption):

        if menuOption == 'quick':
            print('Please enter a race for your character')
            race = input()
            races = self.races

            races = [i.lower() for i in races]

            if race.lower() not in races:
                race_options = ', '.join(i for i in self.races)
                print(race + ' is not a valid race option.\n'
                             'Please select a race from the following:\n'
                      + race_options)
            else:
                character.race = race