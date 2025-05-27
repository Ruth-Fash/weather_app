#    → Show current weather + forecast
from geolocation_module import get_lon_lat_location
import os
import requests


def get_location_weather(lat, lon, api_key, units):

    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units={units}"
    response = requests.get(url) # get request
    data = response.json() # data from request

    #Extract relevant information
    temperature_current = data["main"]["temp"]
    temperature_min = data["main"]["temp_min"]
    temperature_max = data["main"]["temp_max"]
    temperature_feels_like = data["main"]["feels_like"]
    humidity = data["main"]["humidity"]
    description = data["weather"][0]["description"]

    unit_symbol = "°C" if units == "metric" else "°F"


    print("Weather Summary".center(35))
    print("-" * 35)
    print(f"{'Current Temperature:':<20} {temperature_current}{unit_symbol}")
    print(f"{'Min Temperature:':<20} {temperature_min}{unit_symbol}")
    print(f"{'Max Temperature:':<20} {temperature_max}{unit_symbol}")
    print(f"{'Feels Like:':<20} {temperature_feels_like}{unit_symbol}")
    print(f"{'Humidity:':<20} {humidity}%")
    print(f"{'Weather:':<20} {description}")
    print("-" * 35)
