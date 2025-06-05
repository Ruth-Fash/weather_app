import os
import requests
from modules.geolocation_module import get_country_code, get_location_name, get_lon_lat_location
from datetime import datetime


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


    



def get_hourly_weather(lat, lon, api_key, units):

    url = f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={api_key}&units={units}&cnt=8"
    response = requests.get(url) # get request
    data = response.json() # data from request
    
    #Extract relevant information
    location_name = (data["city"]["name"])
    date_only = (data["list"][0]["dt_txt"].split()[0])

    print((f"Hourly Forecast for {location_name} - {date_only}"))
    print("-" * 35)
    print(f"{'Time':<8} {'Temp (°C)':<10} {'Description':<15}")
    print("-" * 35)
    for forecast in data["list"]:
        full_time = (forecast["dt_txt"])
        time_only = full_time.split()[1][:5]
        temp = forecast["main"]["temp"]
        weather_desc = forecast["weather"][0]['main']
        print(f"{time_only:<8} {temp:<10.1f} {weather_desc:<15}")



def date_input():
    while True:
        user_input = input("Enter date you would like to search (yyyy-mm-dd): ")

        if not user_input:
            print ("Date does not exist or data is missing. Please try again in the correct format (yyyy-mm-dd).")
            continue
        try:
            # Try to parse the date
            datetime.strptime(user_input, "%Y-%m-%d")
            # If parsing succeeds, return the valid date string
            return user_input
        except ValueError:
            print("Invalid date format or non-existent date. Please try again in the format yyyy-mm-dd.")
    



def specific_date(lat, lon, api_key, date):
    specific_date_url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{lat},{lon}/{date}?unitGroup=uk&key={api_key}"
    response = requests.get(specific_date_url)
    data = response.json()
    
    day = data['days'][0]
    date = day['datetime']
    temp_max = day['tempmax']
    temp_min = day['tempmin']
    temp_avg = day['temp']

    print(f"\n🕰️ Weather report from {date} 🕰️")
    print(f"On this day, the temperature ranged from {temp_min}° to {temp_max}°, averaging around {temp_avg}°.")

    if temp_max > 25:
        print("It was a warm day! Perfect for some sunshine. ☀️")
    elif temp_max < 10:
        print("Quite chilly that day — a day to bundle up! 🧥")
    else:
        print("Mild weather — not too hot, not too cold. Just right! 🌤️")
 



