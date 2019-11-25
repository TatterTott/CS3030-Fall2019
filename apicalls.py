from bs4 import BeautifulSoup
from subprocess import Popen
import urllib.request
import requests
import os
import sys
import json

def main():
    url = "http://dnd5eapi.co/api/classes"

    response = requests.get(url)
    response.raise_for_status()
    weatherData = json.loads(response.text)
    print(weatherData['results'])

    for elem in weatherData['results']:
        print (elem['name'])
main()
