import pycountry
import requests


def get_country_code():
    user_input = input("Enter country name or code: ")
    try:
        country = pycountry.countries.lookup(user_input)
        print(f"Country Selected...{country.alpha_2}")  # standardized 2-letter code
        return country.alpha_2

    except LookupError:
        print("Country not found")
        return None

def get_city_name():
    while True:
        city_name = input("Enter city name ")
        if not city_name:
            print("Cannot leave field empty")
            continue
        return city_name


def get_lon_lat():
    while True:
        try:
            api_key = "9d155096c4339d42978deb57ae2027e2"
            city_name = get_city_name()
            country_code = get_country_code()

            url = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name},{country_code}&limit=1&appid={api_key}"

            response = requests.get(url)
            data = response.json()
            first_location = data[0]  # get first dict
            lat = first_location['lat']
            lon = first_location['lon']

            return lat,lon
        
        except requests.exceptions.RequestException as e:
            print(f"Network or API error: {e}. Please try again.")
        except (IndexError, KeyError):
            print("City does not exist or data is missing. Please try again.")






