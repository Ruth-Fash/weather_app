import os
import requests
import pycountry
from datetime import datetime

def location_exists(location_name, country_code=None):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": f"{location_name},{country_code}" if country_code else location_name,
        "appid": "9d155096c4339d42978deb57ae2027e2"
    }
    try:
        response = requests.get(base_url, params=params)
        if response.status_code == 200:
            return True
        elif response.status_code == 404:
            return False
        else:
            print(f"API error: {response.status_code}")
            return False
    except requests.RequestException as e:
        print(f"Network error: {e}")
        return False
    

def get_lon_lat_location(location, code, api_key):
    while True:
        try:
            url = f"http://api.openweathermap.org/geo/1.0/direct?q={location},{code}&limit=1&appid={api_key}"

            response = requests.get(url)
            data = response.json()

            if not data:
                print("Location does not exist or data is missing. Please try again.")
                continue # retry

            first_location = data[0]  # get first dict
            lat = first_location['lat']
            lon = first_location['lon']
            return lat,lon
        
        except requests.exceptions.RequestException as e:
            print(f"Network or API error: {e}. Please try again.")
            continue


def get_country_code():
    while True:
        user_input = input("Enter country name or code: ")
        try:
            country = pycountry.countries.lookup(user_input.strip())
            print(f"Country Selected...{country.alpha_2}")  # standardized 2-letter code
            return country.alpha_2.upper()

        except LookupError:
            print("Country not found, try again")


def get_location_name(country_code):
    while True:
        location_name = input("Enter Location or town name: ")
        print (f"You Selected: {location_name}")
        if not location_name:
            print("Cannot leave field empty")
            continue
        elif location_exists(location_name, country_code):
            return location_name.title().strip()
        else:
            print("Location not found. Please try again.")


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
    

def specific_date(lat, lon, api_key, date): # using different weather api 
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
 



