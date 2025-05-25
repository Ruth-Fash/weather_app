import requests
from  language_module import select_langauge
from geolocation_module import get_country_code, get_lon_lat
import os
api_key = "9d155096c4339d42978deb57ae2027e2"


menu = ['City weather', 'Town weather', 'Settings']



lat,lon = get_lon_lat() # get lat lon depenign on city and country code entered
os.system('clear') # clear screen

url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric"
response = requests.get(url) # get request
data = response.json() # data from request

#Extract relevant information
temperature_current = data["main"]["temp"]
temperature_min = data["main"]["temp_min"]
temperature_max = data["main"]["temp_max"]
temperature_feels_like = data["main"]["feels_like"]
humidity = data["main"]["humidity"]
description = data["weather"][0]["description"]

print(f"Current Temperature: {temperature_current}°C")
print(f"Min Temperature: {temperature_min}°C")
print(f"Max Temperature: {temperature_max}°C")
print(f"Feels Like: {temperature_feels_like}°C")
print(f"Humidity: {humidity}%")
print(f"Weather: {description}")


# if "cloud" in description:
#     print("It's cloudy today.")
# else:
#     print("🌞 No clouds today!")

