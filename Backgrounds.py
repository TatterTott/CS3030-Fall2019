import requests
import json

# Grabbing the info from the API
response = requests.get('https://open5e.com/sections/backgrounds',
Backgrounds = BackgroundObject)
print(response.json())

def get_info():

    dict = {'Proficiencies', 'Languages', 'Equipment', 'Characteristics', 'Background'}
    dict['Proficiencies'] = 'https://open5e.com/sections/backgrounds'
    dict['Languages'] = 'https://open5e.com/sections/backgrounds'
    dict['Characteristics'] = 'https://open5e.com/sections/backgrounds'
    dict['Background'] = 'https://open5e.com/sections/backgrounds'

    return [{'label': l, 'url': u} for l, u in dict.iteritems()]

get_info()

# I am dumping all the info word for word
# Containing python's dictionary, lists, strings, and integers
# def print(obj):
#     # create a formatted string
#     backroundInfo = json.dumps(obj, sort_keys=True, indent=4)
#     print(backroundInfo)
# # just so that its easier to read
#
# while True:
#     print("Select what you would like to be?(Acolyte, Con Artist or Scoundrel)")
#     while True:
#         user_picks = int(input())
#         if user_picks == Acolyte:
#             Acolyte = {'Proficiencies', 'Languages', 'Equipment', 'Characteristics', 'Background'}
#             print('You have chosen Acolyte', backroundInfo)
#             continue
#         elif user_picks == ConArtist:
#             ConArtist = {'Proficiencies', 'Languages', 'Equipment', 'Characteristics', 'Background'}
#             print('You have chosen ConArtist', backroundInfo)
#             continue
#         else:
#             user_picks == Scoundrel
#             Scoundrel = {'Proficiencies', 'Languages', 'Equipment', 'Characteristics', 'Background'}
#             print('You have chosen Scoundrel', backroundInfo)
#             break

