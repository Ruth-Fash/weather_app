from modules.weather_module import get_hourly_weather,  get_location_weather, get_lon_lat_location, get_location_name
from modules.settings_module import load_settings, load_default
import os

api_key = "9d155096c4339d42978deb57ae2027e2"
menu = ['Search Weather by Location', 'My Saved Locations', 'Historical Weather Lookup', 'Settings', 'Exit']
settings = load_settings()


def user_next_action(lat_location, lon_location, api_key):
    while True:
        user_choice = input(
            "\nWhat would you like to do next?\n"
                        "Enter\n"
            "'H' to see the hourly forecast,\n"
            "'F' to see the 5-day forecast,\n"
            "'Y' to search for another location,\n"
            "'N' to return to the main menu: "
        ).strip().upper()

        if user_choice == "H":
            os.system('clear')
            hourly_weather = get_hourly_weather(lat_location, lon_location, api_key, settings["units"])
            continue

        elif user_choice == "F":
            os.system('clear')
            print("5-day forecast under construction....")
            continue # Back to main menu

        elif user_choice == 'Y':
            os.system('clear')
            break # Restart the inner loop to search for another city

        elif user_choice == "N":
            os.system('clear')
            print("returning to main menu...")
            return "main_menu"

        else:
            os.system('clear')
            print("Invalid input. Please enter H, F, Y, or N.")

def main_menu_list():
    os.system('clear') # clear screen
    print("\n" + "=" * 37)
    print(" WEATHER APP ".center(37, "="))
    print("=" * 37 + "\n")

    for index, options in enumerate(menu, 1):
        print (f"{index}. {options}")

    print( "=" * 37 )

def get_and_show_weather():
        os.system('clear') # clear screen
        
        settings = load_settings()  # load setting for temp

        settings_default = load_default() # load setting for defauly location 
        
        city = settings_default.get("city")
        code = settings_default.get("country_code")
        lat1, lon1 = get_lon_lat_location(city, code, api_key)

        print(f"Location: {city} | Country Code: {code} ") 
        get_location_weather(lat1, lon1, api_key, settings["units"])

        return settings, settings_default