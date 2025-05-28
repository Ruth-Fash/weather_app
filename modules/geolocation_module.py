import pycountry
import requests



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
        if location_exists(location_name, country_code):
            return location_name.title().strip()
        else:
            print("Location not found. Please try again.")