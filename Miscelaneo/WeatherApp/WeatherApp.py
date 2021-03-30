import requests
from pprint import pprint
##This program get the current weather for the city that is given in the input.

Api_key = ''

city = input("Enter a city: ")

base_url = "https://api.openweathermap.org/data/2.5/weather?appid=" + Api_key + "&q=" + city

weather_data=requests.get(base_url).json()

pprint(weather_data)
