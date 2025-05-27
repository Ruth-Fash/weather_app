from geolocation_module import get_country_code
import requests


def get_hourly_weather(lat, lon, api_key):

    url = f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={api_key}&units=metric&cnt=8"
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
