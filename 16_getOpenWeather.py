# Program that prints the weather forecast for a location entered on the command line

import requests, json, sys

APPID = '285595b2ceecb81516599c40d2267572'

# compute location from command line arguments
if len(sys.argv) < 2:
    print('Usage: getOpenWeather.py city_name, 2-letter_country_code')
    input('Press enter to continue...')
    sys.exit()

location = ''.join(sys.argv[1:])

# Download the json data from OpenWeatherMap.org's API
url = 'https://api.openweathermap.org/data/2.5/forecast/daily?q={}&cnt=3&APPID={}'.format(location,
APPID)

response = requests.get(url)
response.raise_for_status()

print(response.text)

# TODO: Load json data into a Python variable