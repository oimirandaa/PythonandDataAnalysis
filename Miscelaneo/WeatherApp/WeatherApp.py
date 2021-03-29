import requests
from pprint import pprint

Api_key = '545c200c5d4d6d3eb8bf18fb819ad3cc'

city = input("Enter a city: ")

base_url = "https://api.openweathermap.org/data/2.5/weather?appid=" + Api_key + "&q=" + city

weather_data=requests.get(base_url).json()

pprint(weather_data)
